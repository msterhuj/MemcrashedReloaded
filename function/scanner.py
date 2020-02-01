import socket
import netaddr


def scan(input_ip):
    print("Init scan")
    for ip in list(netaddr.IPNetwork(input_ip)):
        if isMemcache(str(ip)):
            print("Open !" + str(ip))
        else:
            print("Close" + str(ip))


def isMemcache(ip):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(1)
    try:
        soc.connect((ip, 11211))
        soc.shutdown(2)
        return True
    except:
        return False
