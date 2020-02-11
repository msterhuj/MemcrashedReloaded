import socket
import iptools
from function import filemanager

def scan(input_ip):
    print("Init scan")
    ips = iptools.IpRange(input_ip).__iter__()
    while True:
        try:
            ip = iptools.next(ips)
            filemanager.save_ip(isMemcache(ip), str(ip))
        except StopIteration:
            print("StopIteration")
            break



def isMemcache(ip):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(1)
        soc.connect((ip, 11211))
        soc.shutdown(2)
        return True
    except:
        return False
