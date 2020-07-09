import click
import iptools
import os
from utils.lib import console
from utils.TouDoumScanner import TouDoumScanner
from utils.TouDoumAttack import TouDoumAttack


@click.group()
def cli_scanner():
    pass


@click.group()
def cli_attack():
    pass


@cli_scanner.command()
@click.option('--ip', type=iptools.IpRangeList, help='ip range to scan with cidr')
@click.option('--ipfile', type=str, help='input file with a ip list (one ip by line)')
@click.option('--shodan', type=str, help="get ip list with shodan.io for probable vulns enter api key")
@click.option('--timeout', default=1, help='timeout for connection (default 1)')
@click.option('--skip-private', 'skip_private', is_flag=True, type=bool, help='skip private ip for scan')
@click.option('--memcached', is_flag=True, type=bool, help='enable scan for memcached protocol')
@click.option('--ntp', is_flag=True, type=bool, help='enable scan for ntp protocol')
@click.option('--dns', is_flag=True, type=bool, help='enable scan for dns protocol')
@click.option('--output', type=str, help='output file name')
@click.option('--verbose', is_flag=True, type=bool, help='verbose scan information (show passed ip or other error)')
@click.option('--threads', default=1, help='WIP')
def scanner(ip, ipfile, shodan, timeout, skip_private, memcached, ntp, dns, output, verbose, threads):
    """
        Scanner for detect udp port on memcached, dns and ntp
    """
    sc = TouDoumScanner(ip, ipfile, shodan, skip_private, memcached, ntp, dns, timeout, verbose, threads)
    sc.set_file_name(output)
    sc.init()
    sc.send()


@cli_attack.command()
@click.option('--amp', type=str, help='list of server used for amplification attack on json format')
@click.option('--memcached', is_flag=True, type=bool, help='use memcached protocol for attack')
@click.option('--ntp', is_flag=True, type=bool, help='use ntp protocol for attack')
@click.option('--dns', is_flag=True, type=bool, help='use dns protocol for attack')
@click.option('--power', type=int, help='numbers of packet\'s send for one ip')
@click.option('--target-ip', 'target_ip', type=str, help='target ip')
@click.option('--target-port', 'target_port', type=int, help='target port')
@click.option('--verbose', is_flag=True, type=bool, help='verbose scan information (show scapy packet send)')
def attack(amp, memcached, ntp, dns, power, target_ip, target_port, verbose):
    """
        Attack server with spoofed udp packed
    """
    ak = TouDoumAttack(amp, memcached, ntp, dns, power, target_ip, target_port, verbose)
    ak.run()


cli = click.CommandCollection(sources=[cli_scanner, cli_attack])

if __name__ == '__main__':
    click.clear()
    console.banner()
    if os.getuid() == 0:
        cli()
    else:
        console.error("You need to be run this script with root privileges")
