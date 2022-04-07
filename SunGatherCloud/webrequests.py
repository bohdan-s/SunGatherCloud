import sys
import requests
import json

from Crypto.Cipher import AES

username=''
password=''

## Set up pading for AES
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
obj = AES.new('webXXXXXXXXXXXXX', AES.MODE_ECB, '')

# Set up cookies
req_session = requests.Session() 
req_session.cookies.set("cloudId", "7")
req_session.cookies.set("isRandomPwd", "false")
req_session.cookies.set("isMustInputEmail", "1")
req_session.cookies.set("lang", "en_US")
req_session.cookies.set("isAgg", "1")
req_session.cookies.set("globalWeakenTip", "1")
req_session.cookies.set("homePagePrompt", "1")
req_session.cookies.set("isAustralia", "1")
req_session.cookies.set("noLoadPsListTip", "1")
req_session.cookies.set("remember", "")
req_session.cookies.set("userLang", "en_US")
req_session.cookies.set("username", "")
req_session.cookies.set("sid", "1649293299618") #1649221562598
req_session.cookies.set("user_token", "")
req_session.cookies.set("did", "17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39") #17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39
#req_session.cookies.set("zg_did", '{"did": "17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39"}') #%7B%22did%22%3A%20%2217ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39%22%7D

'''
zg_f2404cb263bd4b93a6c356cbf58d91e1=%7B%22sid%22%3A%201649293299618%2C%22updated%22%3A%201649293313848%2C%22info%22%3A%201649211905887%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201649293299618%2C%22cuid%22%3A%20%220_261188%22%7D;
zg_9e25827ce33c49648d54e923513dbf28=%7B%22sid%22%3A%201649221584731%2C%22updated%22%3A%201649221637650%2C%22info%22%3A%201649221584734%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22au.isolarcloud.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fportalau.isolarcloud.com%2F%23%2F%3Ftoken%3D261188_225e12c20d0b46d987525192f489ae52%26isRandomPwd%3Dfalse%26isAbroad%3D1%26cloudId%3D7%26noMenu%3D0%26microGateWayUrl%3Dhttps%3A%2F%2Faugateway.isolarcloud.com%26apiUrl%3Dhttps%3A%2F%2Fauapi.isolarcloud.com%26baseUrl%3Dhttps%3A%2F%2Fau.isolarcloud.com%26did%3D17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39%26sid%3D1649221562598%26lang%3Den_US%22%7D; 
_uab_collina=164921196375545035542415",
'''

##### Log in and get Auth Token
req_headers = {
            "Host": "au.isolarcloud.com",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            #"_ismd5": "1",
            "_browser_version": "15.1",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "_did": "17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39",
            "x-requested-with": "XMLHttpRequest",
            "_pl": "js",
            "accept-language": "en-AU,en;q=0.9",
            "origin": "https://au.isolarcloud.com",
            "_browser_brand": "safari",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
            "_sid": "1649306275281",
            "referer": "https://au.isolarcloud.com/"
        }

req_params = "userAcct=" + username + "&userPswd=" + password + "&sysCode=portal&sign="
r = req_session.post(f'https://www.isolarcloud.com/userLoginAction_login', params=req_params, headers=req_headers)
#print(r.request.headers)
#print(r.text)
response = json.loads(str(r.text))
user_token = response['user_token']
print("Token Retrieved:" + user_token)

##### Get current timestamp TODO just geneate this?
r = req_session.post(f'https://augateway.isolarcloud.com/v1/timestamp')
timestamp = json.loads(str(r.text))['result_data']
print("Timestamp Retrieved:" + timestamp)

print('---------')

#### User Service Login
req_data = '{"service":"login","login_type":2,"sys_code":200,"api_key_param":{"timestamp":'+timestamp+',"nonce":"Zig4IX0FEl8iCzNCIc3FiwyiUMXe0jcp"},"appkey":"B0455FBE7AA0328DB57B59AA729F05D8","token":"'+user_token+'","lang":"_en_US"}'
print("Params: " + req_data)
req_data = obj.encrypt(pad(req_data))
req_data = (bytes(req_data).hex())
print("Encrypted Params: " + req_data)

req_header = { 
            "Host": "augateway.isolarcloud.com",
            "_browser_brand": "safari",
            "referer": "https://portalau.isolarcloud.com/",
            "_browser_version": "15.1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
            "_did": "17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39",
            "x-access-key": "9grzgbmxdsp3arfmmgq347xjbza4ysps", #Request is not encrypted
            "sys_code": "200",
            "x-random-secret-key": "IZIAY4l/ZesqeyLLtKfdzI/Oqa5CrL31NEuVH/O5eZ6ef0CmUBhIFXVA3SP41rFdlmGLJe4IRX12WL3iamgFZGH2awlbrz6F+MVfDETot1y0Sjyjd/ePjjiLbHiKoMJ9BHIXiusarnjg7bqdfOxxwU+uvx8DWLaQBNOupwiONaE=", #Request parameters must be in json format
            "origin": "https://portalau.isolarcloud.com",
            "_vc": "2022022801",
            "x-limit-obj": "jkYRX+eOtBwNQFR8vBnPxKSeufwZ/HNGqBT1+DAE4bu+7u4rUgJil/+L6ZrTDAR+Oqazl+QM1WI+DovQMA4Fw27SD8rzZ6X+8AykDDGrPg6FpiXGM2rv9fk0SF0RbPwKqbGpQNozCGmERaKTX5eOggcfWNTDbNr8FinidwHz3M0=",
            "accept-language": "en-AU,en;q=0.9",
            "_sid": "1649306275281",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "_did2": "17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39",
            "x-client-tz": "GMT+10",
            "_pl": "js"
        }


r = req_session.post(f'https://augateway.isolarcloud.com/v1/userService/login', data=req_data, headers=req_header)
print("Encrypted Reponse:" + r.text)

dec_text = obj.decrypt(bytes.fromhex(r.text)).decode()
print("Decrypted Reponse:" + dec_text)

sys.exit()

#### MQTT Subscribe
#req_data = '{"service":"reqSecondDataSubscribeBySN","sn":"B2131700719","is_renew":0,"sys_code":200,"api_key_param":{"timestamp":1649293331253,"nonce":"KEkcYRAHp5bMJFiyBvoRUBUhrQHs9CL9"},"appkey":"B0455FBE7AA0328DB57B59AA729F05D8","token":"261188_5850f59ac8d74d45bc7272cec488d663","lang":"_en_US"}'
req_data = '{"service":"reqSecondDataSubscribeBySN","sn":"B2131700719","is_renew":0,"sys_code":200,"api_key_param":{"timestamp":' + timestamp + ',"nonce":"KEkcYRAHp5bMJFiyBvoRUBUhrQHs9CL9"},"appkey":"B0455FBE7AA0328DB57B59AA729F05D8","token":"' + user_token + '","lang":"_en_US"}'
req_data = obj.encrypt(pad(req_data))
req_data = (bytes(req_data).hex())
print("Enc_Params:" + req_data)

req_header = { 
        "Host": "augateway.isolarcloud.com",
        "_browser_brand": "safari",
        "referer": "https://portalau.isolarcloud.com/",
        "_browser_version": "15.1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
        #"_did": "17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39",
        "x-access-key": "9grzgbmxdsp3arfmmgq347xjbza4ysps",
        "sys_code": "200",
        "x-random-secret-key": 'bOIUusf4nuylyu0+tP1kVGqKWC/ng5/Gc/0u/w5WSXXnfWhF7ClhuACoE6ROjbpXapiOI+cIAej93XfQ69wCDRiTyNW/65/1d0jyrM0mUsAQbJxL8B+4DmWZo4WxA/2NzQ6TpYU7wk3XwCH0VR4633ZAKR+RZYyylW8I42aJzWM=',
        "origin": "https://portalau.isolarcloud.com",
        #"_vc": "2022022801",
        "x-limit-obj": 'nWvIF7/i0MeoNjDXD7GLZwRq1chQEnToYn4iZ03A4RrOL/v0j7QDkAxgtV3gzlerM12odhRC7yeih2RRi+FQuzMXwkfhU6bZI2JM4lDHkLJhMmBt/Sky5fCm5D4KunAhFn//pBIO4phDgr61iYOAW6GiFo8VwrLVetMdd29Au7E=',
        "accept-language": "en-AU,en;q=0.9",
        "_sid": "1649293299618",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        #"_did2": "17ffcb09757a48-085e5dc37378798-3f62684b-13c680-17ffcb09758d39",
        "x-client-tz": "GMT+10",
        "_pl": "js"
        }

r = req_session.post(f'https://augateway.isolarcloud.com/v1/commonService/reqSecondDataSubscribeBySN', data=req_data, headers=req_header)
print(r.text)
dec_text = obj.decrypt(bytes.fromhex(r.text)).decode()
print("Decrypted:" + dec_text)

