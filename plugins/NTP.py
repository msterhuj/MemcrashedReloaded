import ntplib


class Plugin:
    name = "DNS"
    description = "scan and use dns vulnerable server for amp attack"
    author = "@Msterhuj"
    protocol = "UDP"

    def __init__(self):
        pass

    def scan(ip: str, timeout: int):
        c = ntplib.NTPClient()
        try:
            return c.request(ip, timeout) is not None
        except KeyboardInterrupt:
            print("User request Ctrl + C Quitting.")
            exit(-1)
        except:
            return False

    def attack(self):
        pass
