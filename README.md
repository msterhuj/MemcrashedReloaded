# TouDoum-DDoS-Exploit

## DISCLAIMER
> This script can scan ip's or retrieve them from shodan and then scan them for vulnerabilities and use them to carry out large ddos attacks.
> This script uses the amplification technologies of:
> * memcached [POC](https://www.cloudflare.com/learning/ddos/memcached-ddos-attack/)
> * ntp [POC](https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/)
> * dns [POC](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)
>
>I am NOT responsible for damages caused or crimes committed by the use of this tool. 

## Installation

### Remember
> you need to run this script with root privileges and run this tool on machine with public ip for attack (spoffing)
```bash
git clone https://github.com/msterhuj/TouDoum-DDoS-Exploit
cd TouDoum-DDoS-Exploit
pip3 install -r requirements.txt
```

## Using
```bash
python3 TouDoum.py
```
```
▄▄▄█████▓ ▒█████   █    ██    ▓█████▄  ▒█████   █    ██  ███▄ ▄███▓    ▐██▌ 
▓  ██▒ ▓▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▒██▒  ██▒ ██  ▓██▒▓██▒▀█▀ ██▒    ▐██▌ 
▒ ▓██░ ▒░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██░  ██▒▓██  ▒██░▓██    ▓██░    ▐██▌ 
░ ▓██▓ ░ ▒██   ██░▓▓█  ░██░   ░▓█▄   ▌▒██   ██░▓▓█  ░██░▒██    ▒██     ▓██▒ 
  ▒██▒ ░ ░ ████▓▒░▒▒█████▓    ░▒████▓ ░ ████▓▒░▒▒█████▓ ▒██▒   ░██▒    ▒▄▄  
  ▒ ░░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░    ░▀▀▒ 
    ░      ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ░  ░      ░    ░  ░ 
  ░      ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░ ░ ░ ░ ▒   ░░░ ░ ░ ░      ░          ░ 
             ░ ░     ░           ░        ░ ░     ░            ░       ░    
                               ░                
                    ---===[Author: @MsterHuj]===---
                          --==[Ver : X.X]==--

Usage: TouDoum.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  attack   Attack server with spoofed udp packed
  scanner  Scanner for detect udp port on memcached, dns and ntp
```
## Features
* scan the plage ip
* get ip from shodan.io
* import ip from file (one ip per line)
* scan by service type (memcache, ntp, dns) on udp
* attack with multi thread and multiple service type scanned before

## Future update
* add multi task for scan
* rewrite function for get ip on shodan.io

## Credit for dev
* [Dns UDP port checker](https://stackoverflow.com/a/51970598)
