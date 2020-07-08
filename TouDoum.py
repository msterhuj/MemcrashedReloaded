import click
import iptools
from utils.lib import console
from utils.TouDoumScanner import TouDoumScanner


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
def attack():
    """
        [WIP] i need to finish the scanner before do dev this part :)
        Attack for overwhelm the targeted network with memcached, dns and ntp
        This script part need a ip list on input
    """
    print(
        "[WIP] i need to finish the scanner before do dev this part :)\nAttack for overwhelm the targeted network with memcached, dns and ntp\nThis script part need a ip list on input")


cli = click.CommandCollection(sources=[cli_scanner, cli_attack])

if __name__ == '__main__':
    click.clear()
    console.banner()
    cli()
