import socket


def memcache_udp(ip, timeout):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(timeout)
    try:
        client.sendto(bytes("\x00\x00\x00\x00\x00\x01\x00\x00\x73\x74\x61\x74\x73\x0d\x0a", encoding='utf8'),
                      (ip, 11211))
        data = client.recvfrom(4096)
        length = len(data[0])
        return length > 200
    except socket.timeout:
        return False
    except KeyboardInterrupt:
        print("User request Ctrl + C Quitting.")
        exit(-1)
    finally:
        client.close()


if __name__ == '__main__':
    print("Wrong file run TouDoum.py --help")
