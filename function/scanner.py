import socket
import iptools
from function import filemanager
from function import settings

private = iptools.IpRangeList(
    '0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24', '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4', '240.0.0.0/4', '255.255.255.255/32'
)



def scan(input_ip):
    print("Init scan")
    time_out = settings.load().getTimeOut()
    ips = iptools.IpRange(input_ip).__iter__()
    while True:
        try:
            ip = iptools.next(ips)
            if ip not in private:
                filemanager.save_ip(checkMemcache(ip), str(ip))
            else:
                print("Skipped private ip '" + ip + "'")
        except StopIteration:
            print("Finish scan !")
            break


def checkMemcache(ip):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(time_out)
        soc.connect((ip, 11211))
        soc.shutdown(2)
        return True
    except:
        return False
