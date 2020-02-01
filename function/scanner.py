import socket
import netaddr
from function import filemanager


def scan(input_ip):
    print("Init scan")
    for ip in netaddr.IPNetwork(input_ip):
        filemanager.save_ip(isMemcache(input_ip), str(input_ip))


def isMemcache(ip):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(1)
    soc.connect((ip, 11211))
    soc.shutdown(2)
    return True
