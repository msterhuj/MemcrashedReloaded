import requests
import socket
import random
import struct
import ntplib
import iptools

ip_private = iptools.IpRangeList(
    '0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24', '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4', '240.0.0.0/4', '255.255.255.255/32'
)

def main():
    while True:
        r = requests.get('http://server/next')
        if r.text not in ip_private:
            print(r.text)
            if r.text != "end":

                data = {
                    'ip': r.text,
                    'memcache': memcache_udp(r.text, 1),
                    'dns': dns_udp(r.text, 1),
                    'ntp': ntp_udp(r.text, 1)
                }

                requests.post('http://server/save', json=data)

            else:
                print("End of iteration")
                exit(0)


# memcache checker
def memcache_udp(ip: str, timeout: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(timeout)
    try:
        client.sendto(bytes("\x00\x00\x00\x00\x00\x01\x00\x00\x73\x74\x61\x74\x73\x0d\x0a", encoding='utf8'),
                      (ip, 11211))
        data = client.recvfrom(4096)
        length = len(data[0])
        return length > 200
    except:
        return False
    finally:
        client.close()


# dns udp checker
# credit : https://stackoverflow.com/a/51970598
class SendDNSPkt:
    def __init__(self, url: str, server_ip: str, timeout: int, port=53):
        self.url = url
        self.server_ip = server_ip
        self.port = port
        self.timeout = timeout

    def send_pkt(self):
        pkt = self._build_packet()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(self.timeout)
        sock.sendto(bytes(pkt), (self.server_ip, self.port))
        data, addr = sock.recvfrom(1024)
        sock.close()
        return data

    def _build_packet(self):
        randint = random.randint(0, 65535)
        packet = struct.pack(">H", randint)  # Query Ids (Just 1 for now)
        packet += struct.pack(">H", 0x0100)  # Flags
        packet += struct.pack(">H", 1)  # Questions
        packet += struct.pack(">H", 0)  # Answers
        packet += struct.pack(">H", 0)  # Authorities
        packet += struct.pack(">H", 0)  # Additional
        split_url = self.url.split(".")
        for part in split_url:
            packet += struct.pack("B", len(part))
            for s in part:
                packet += struct.pack('c', s.encode())
        packet += struct.pack("B", 0)  # End of String
        packet += struct.pack(">H", 1)  # Query Type
        packet += struct.pack(">H", 1)  # Query Class
        return packet


def dns_udp(ip: str, timeout: int, domain_name="www.google.com"):
    s = SendDNSPkt(domain_name, ip, timeout)
    status = False
    for _ in range(5):  # udp is unreliable.Packet loss may occur
        try:
            s.send_pkt()
            return True
        except:
            return False
    return status


# end for credit for https://stackoverflow.com/a/51970598
# just a little edited for match with scanner


# ntp udp checker
def ntp_udp(ip: str, timeout: int):
    c = ntplib.NTPClient()
    try:
        return c.request(ip, timeout) is not None
    except:
        return False


if __name__ == '__main__':
    main()
