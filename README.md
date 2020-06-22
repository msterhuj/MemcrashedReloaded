# [WIP] MemcrashedReloaded

## Installation
```bash
git clone https://github.com/msterhuj/MemcrashedReloaded
cd MemcrashedReloaded
pip3 install -r requirements.txt
```

## Using
```bash
python3 MemcrashedReloaded.py --help
```
```
Usage: MemcrashedReloaded.py [OPTIONS]

  !\ I am not responsible for any damages caused by using this tool. /!

Options:
  --ip IPRANGELIST   ip range to scan with cidr
  --timeout INTEGER  timeout for connection (default 1)
  --scan-private     skip private ip for scan
  --output TEXT      output file
  --verbose          verbose scan information (show passed ip or other error)
  --help             Show this message and exit.
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