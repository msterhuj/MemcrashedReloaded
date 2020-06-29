import click
import iptools
from utils import scan
from utils import data
from utils import console

scan_used = []

private = iptools.IpRangeList(
    '0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24', '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4', '240.0.0.0/4', '255.255.255.255/32'
)


@click.group()
def cli_scanner():
    pass


@click.group()
def cli_attack():
    pass


@cli_scanner.command()
@click.option('--ip', type=iptools.IpRangeList, help='ip range to scan with cidr')
@click.option('--shodan', type=str, help="get ip list with shodan.io for probable vulns enter api key")
@click.option('--timeout', default=1, help='timeout for connection (default 1)')
@click.option('--scan-private', 'scan_private', is_flag=True, type=bool, help='skip private ip for scan')
@click.option('--memcached', is_flag=True, type=bool, help='enable scan for memcached protocol')
@click.option('--ntp', is_flag=True, type=bool, help='enable scan for ntp protocol')
@click.option('--dns', is_flag=True, type=bool, help='enable scan for dns protocol')
@click.option('--output', help='output file name')
@click.option('--verbose', is_flag=True, type=bool, help='verbose scan information (show passed ip or other error)')
@click.option('--threads', default=1, help='WIP')
def scanner(ip, shodan, timeout, scan_private, memcached, ntp, dns, output, verbose, threads):
    """
        Scanner for detect udp port on memcached, dns and ntp
    """

    # check if type scan is set
    if not memcached and not ntp and not dns:
        print("[*] Error : no type scan specified")
        exit(-1)
    else:

        if memcached:
            scan_used.append("memcached")
        if dns:
            scan_used.append("dns")
        if ntp:
            scan_used.append("ntp")

        # check if ip is set
        if ip is not None and shodan is None:

            # all right print configuration for scan and run it
            print("-" * 40)
            print("Ip to scan       : (error on parse WIP)")  # todo
            print("Scan service     : " + str(scan_used))
            print("Timeout          : " + str(timeout))
            print("Threads          : " + str(threads))
            print("Scan private ip  : " + str(scan_private))
            print("Verbose          : " + str(verbose))
            print("-" * 40)

            # generate ip list and send it to checker
            ips = ip.__iter__()

            while True:
                try:
                    ip = iptools.next(ips)

                    if ip in private:
                        if scan_private:
                            processes_manager(ip, timeout, output, verbose, threads)
                        elif verbose:
                            console.ip_skipped(ip)
                    else:
                        processes_manager(ip, timeout, output, verbose, threads)

                except StopIteration:
                    print("Finish scan ! ")
                    break

        elif shodan is not None and ip is None:
            ips = scan.get_from_shodan(shodan)
            for ip in ips:
                processes_manager(ip, timeout, output, verbose, threads)
        else:
            print("[*] Error no ip or shodan key specified")
            print("[*] Info scanner can't use ip scanner and shodan scanner")
            print("[*] Make your choice :)")
            print("[*] run with --help for get help")
            print("[*] Exiting...")


@cli_attack.command()
def attack():
    """
        [WIP] i need to finish the scanner before do dev this part :)
        Attack for overwhelm the targeted network with memcached, dns and ntp
        This script part need a ip list on input
    """
    print(
        "[WIP] i need to finish the scanner before do dev this part :)\nAttack for overwhelm the targeted network with memcached, dns and ntp\nThis script part need a ip list on input")


def processes_manager(ip: str, timeout: int, output: str, verbose: bool, thread: int):
    if output is not None:
        saver = data.load(output)
    else:
        saver = None
    if thread > 1:
        console.error("[WIP] only mono thread for moment sorry")
    thread_scan(ip, timeout, output, saver, verbose)


def thread_scan(ip: str, timeout: int, output: str, saver: data.Data, verbose: bool):
    if "memcached" in scan_used:
        if scan.memcache_udp(ip, timeout):
            console.ip_found(ip, "Memcached")
            if output is not None:
                saver.add_memcached(ip)
        else:
            if verbose:
                console.ip_not_found(ip, "Memcached")

    if "dns" in scan_used:
        if scan.dns_udp(ip, timeout):
            console.ip_found(ip, "DNS")
            if output is not None:
                saver.add_dns(ip)
        else:
            if verbose:
                console.ip_not_found(ip, "DNS")

    if "ntp" in scan_used:
        if scan.ntp_udp(ip, timeout):
            console.ip_found(ip, "NTP")
            if output is not None:
                saver.add_ntp(ip)
        else:
            if verbose:
                console.ip_not_found(ip, "NTP")

    if saver is not None:
        saver.save()


cli = click.CommandCollection(sources=[cli_scanner, cli_attack])

if __name__ == '__main__':
    click.clear()
    console.banner()
    cli()
