import os
import random
import re
import secrets
import rsa
import sys
import yaml
import json
import time
import base64
import string
import logging
import logging.handlers

import paho.mqtt.client as client
from rsa import common, transform, core, key
from version import __version__

class iSolarCloud():
    def __init__(self):
        self.client = None
        publickey_file = open("public.key", "r") 
        self.publickey = publickey_file.read()
        publickey_file.close

        self.ids = [[]]
        self.ids.pop() # Remove null value from list

    def configure(self, config):
    # Configure MQTT Connection
        logging.info(config)

        if not config['host']:
            logging.info(f"MQTT: Host config is required")
            return False

        if config.get('clientid'):
            clientid = config.get('clientid')
        else:
            clientid = "mqttjs_" + secrets.token_hex(4)

        self.client = client.Client(client_id=clientid,transport=config['transport'])
        self.client.ws_set_options(path=config['basepath'], headers=None)
        self.client.username_pw_set(config['username'], config['password'])
        self.client.tls_set()

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message

        self.client.connect_async(host=config['host'], port=config['port'], keepalive=60)

        self.client.loop_start()
    
        return True

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        logging.info(f"iSolarCloud: Connected to {client._host}:{client._port}")
        self.client.subscribe('seconddata/190/1094861/#', qos=0)
        self.client.subscribe('seconddata/190/B2131700719/#', qos=0)
        

    def on_disconnect(self, client, userdata, rc):
        logging.info(f"iSolarCloud: Server Disconnected code: {rc}")

    def on_subscribe(sefl, client, userdata, mid, granted_qos):
        logging.info(f"iSolarCloud: Subscribed: {mid}")

    def on_message(self, client, userdata, message):
        payload = message.payload.decode('utf-8')
        logging.debug(f"{message.topic}:")
        #logging.debug(f"{payload}")


        msg = self.decrypt(payload)
        logging.debug(msg)
        self.printMessage(msg)

    def printMessage(self, message):

        #print(message)
        print("+-----------------------------------------+")
        print("{:<30} {:<10} {:<1}".format("| " + 'ID',"| " + 'Value', "|"))
        print("+------------------------------+----------+")

        jmsg = json.loads(str(message))
        #print(message)

        for item in jmsg['dataList'][0]['data']:
            found = False
            for id in self.ids:
                if item['id'] == str(id['id']):
                    print("{:<30} {:<10} {:<1}".format("| " + str(id['name']), "| " + str(item['val']), "|"))
                    found = True
                    break
            if found == False:
                print("{:<30} {:<10} {:<1}".format("| " + str(item['id']), "| " + str(item['val']), "|"))

            
        print("+------------------------------+----------+")

    def split(self,thing, chunk_size):
        for i in range(0, len(thing), chunk_size):
            yield thing[i:i + chunk_size]
    
    def decrypt(self, message):
        # load public key
        pkey = rsa.PublicKey.load_pkcs1(self.publickey)

        # get key length
        blocksize = common.byte_size(pkey.n)

        # Add pading to message
        message = message + '=' * (4 - len(message) % 4) if len(message) % 4 != 0 else message
        # Decode url safe base64 the message
        ciphertext = base64.urlsafe_b64decode(message)

        # split into chunks for decryption
        chunked = self.split(ciphertext, blocksize)

        output = ""

        # decrypt
        for chunk in chunked:
            # convert ciphertext
            encrypted = transform.bytes2int(chunk)

            # decrypt (we're using this the "wrong way" so its actually an encrypt operation, but w/e)
            decrypted = core.encrypt_int(encrypted, pkey.e, pkey.n)

            # convert plaintext
            plaintext = transform.int2bytes(decrypted, blocksize).decode('utf-8', errors="replace").replace('\ufffd','')

            output = output + plaintext

        output = re.sub(f'[^{re.escape(string.printable)}]', '', output)

        return output

    def configure_ids(self,idsfile):
        # Load IDs list
        for id in idsfile['ids']:
            self.ids.append(id)

def main():

    configfilename = 'config.yaml'
    logfolder = ''

    logging.info(f'Starting SunGather Cloud Edition {__version__}')

    try:
        configfile = yaml.safe_load(open(configfilename))
        logging.info(f"Loaded config: {configfilename}")
    except Exception as err:
        logging.error(f"Failed: Loading config: {configfilename} \n\t\t\t     {err}")
        sys.exit(1)


    try:
        idsfile = yaml.safe_load(open('ids.yaml'))
        logging.info(f"Loaded IDs: {os.getcwd()}/ids.yaml")
        logging.info(f"IDs file version: {idsfile.get('version','UNKNOWN')}")
    except Exception as err:
        logging.error(f"Failed: Loading IDs: {os.getcwd()}/ids.yaml {err}")
        sys.exit(f"Failed: Loading IDs: {os.getcwd()}/ids.yaml {err}")


    config_sungrow = {
        "log_console": configfile['SunGrowCloud'].get('log_console','WARNING'),
        "log_file": configfile['SunGrowCloud'].get('log_file','OFF'),
        "level": configfile['SunGrowCloud'].get('level',1)
    }

    config_iSolarCloud = {
        "host": configfile['iSolarCloud'].get('host',''),
        "transport": configfile['iSolarCloud'].get('transport',''),
        "port": configfile['iSolarCloud'].get('port',''),
        "username": configfile['iSolarCloud'].get('username',''),
        "password": configfile['iSolarCloud'].get('password',''),
        "basepath": configfile['iSolarCloud'].get('basepath',''),
        "topic": configfile['iSolarCloud'].get('topic',''),
        "clientid": configfile['iSolarCloud'].get('clientid','')
    }



    iSolarCloud_client = iSolarCloud()
    iSolarCloud_client.configure(config_iSolarCloud)
    iSolarCloud_client.configure_ids(idsfile)


    print('end')

    while(True):
        time.sleep(5)


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger('')
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
logger.addHandler(ch)

if __name__== "__main__":
    main()

#sys.exit()