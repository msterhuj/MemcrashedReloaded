# [WIP] TouDoum-DDoS-Exploit

## Installation
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
  attack   [WIP] i need to finish the scanner before do dev this part :)...
  scanner  Scanner for detect udp port on memcached, dns and ntp
```
## Future update
* ~~Add multi scan mod (memcached, ntp, dns)~~
* ~~Add attack mod with option type or all~~
* ~~Add multi save file for type of scan~~
* Add input file ip list for scanner
* Fix multithreading (WIP when you use --thread > 2 the script use all core btw)

## Credit for dev
* [Dns UDP port checker](https://stackoverflow.com/a/51970598)
* [Memcrashed-DDoS-Exploit By 649](https://github.com/649/Memcrashed-DDoS-Exploit)
