# [WIP] TouDom-DDoS-Exploit

## Installation
```bash
git clone https://github.com/msterhuj/TouDom-DDoS-Exploit
cd TouDom-DDoS-Exploit
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
                          --==[Ver : 1.4]==--

Usage: TouDoum.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  attack   [WIP] i need to finish the scanner before do dev this part :)...
  scanner  Scanner for detect udp port on memcached, dns and ntp
```
## Future update
* Changing name of project
* Add multi scan mod (memcached, ntp, dns)
* Add attack mod with option type or all
* Add multithreading (WIP when you use --thread > 2 the script use all core btw)

## Credit for dev
* Scanner part
  * [PyScanSe By Clomez](https://github.com/Clomez/PyScanSe)
  * [Piescan By m57](https://github.com/m57/piescan)
* Attack part
  * [Memcrashed-DDoS-Exploit By 649](https://github.com/649/Memcrashed-DDoS-Exploit)
  * [Saddam-new By S4kur4](https://github.com/S4kur4/Saddam-new)