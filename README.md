<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL3 License][license-shield]][license-url]

<br />
<div align="center">

<h2 align="center">SunGather</h2>

  <p align="center">
    Collect data from Sungrow Inverters using iSolarCloud
    <br />
    <br />
    <a href="https://sungather.app">Website Sungather.app</a>
    ·
    <a href="https://github.com/bohdan-s/SunGatherCloud/issues">Report Bug</a>
    ·
    <a href="https://github.com/bohdan-s/SunGatherCloud/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

<b>Join the Discord Server to discuss, suggestions or for any help: <a href="https://discord.gg/7j2MVsT5wn">SunGather Discord</a></b>

Access data from iSolarCloud connected Sungow Inverter.

Special thanks to [kroncid](https://github.com/kronicd/) for providing the decryption code

Has multiple export locations out of the box:
* PVOutput - Load into PVOutput.org
* InfluxDB - Load data directly into InfluxDB
* Simple webserver showing collected data

<p align="right">(<a href="#top">back to top</a>)</p>

## Raodmap / TO DO


// TO DO


### Built With

* [Python3](https://www.python.org/)

### Requires
* [paho-mqtt](https://pypi.org/project/paho-mqtt/)
* [PyYAML](https://pypi.org/project/PyYAML/)
* [requests](https://pypi.org/project/requests/)
* [influxdb-client](https://pypi.org/project/influxdb-client/)
* [rsa](https://pypi.org/project/rsa/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
# Local

// TO DO

# Docker

// TO DO

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

// TO DO

<p align="right">(<a href="#top">back to top</a>)</p>

### Commandline Arguments

// TO DO

## Exports

A collection of exports are available:

* console:    Output information to console, useful for troubleshooting
* webserver:  Output to a simple website, default http://localhost:8080 or http://\<serverip\>:8080
* mqtt:       Output to a pre-existing MQTT server, needed for Home Assistant integration
* pvoutput:   Output to PVOutput.org, requires account and solar is set up on website first. 
* InfluxDB:   Output directly to InfluxDB, can then be used by Grafana, etc..

## IDs

// TO DO

### Useful Registers:

// TO DO

## Home Assistant setup

// TO DO

<p align="right">(<a href="#top">back to top</a>)</p>

## Tested
* SG7.0RT with WiNet-S Dongle


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GPL3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Sungrow MQTT Decrypter](https://github.com/kronicd/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/bohdan-s/SunGather.svg?style=for-the-badge
[contributors-url]: https://github.com/bohdan-s/SunGather/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bohdan-s/SunGather.svg?style=for-the-badge
[forks-url]: https://github.com/bohdan-s/SunGather/network/members
[stars-shield]: https://img.shields.io/github/stars/bohdan-s/SunGather.svg?style=for-the-badge
[stars-url]: https://github.com/bohdan-s/SunGather/stargazers
[issues-shield]: https://img.shields.io/github/issues/bohdan-s/SunGather.svg?style=for-the-badge
[issues-url]: https://github.com/bohdan-s/SunGather/issues
[license-shield]: https://img.shields.io/github/license/bohdan-s/SunGather.svg?style=for-the-badge
[license-url]: https://github.com/bohdan-s/SunGather/blob/main/LICENSE.txt
