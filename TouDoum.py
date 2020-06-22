import click
import iptools
import socket
import time
import multiprocessing
import scan

time_start = time.time()
scan_used = []
processes = []

private = iptools.IpRangeList(
    '0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24', '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4', '240.0.0.0/4', '255.255.255.255/32'
)

BANNER = '''
▄▄▄█████▓ ▒█████   █    ██    ▓█████▄  ▒█████   █    ██  ███▄ ▄███▓    ▐██▌ 
▓  ██▒ ▓▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▒██▒  ██▒ ██  ▓██▒▓██▒▀█▀ ██▒    ▐██▌ 
▒ ▓██░ ▒░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██░  ██▒▓██  ▒██░▓██    ▓██░    ▐██▌ 
░ ▓██▓ ░ ▒██   ██░▓▓█  ░██░   ░▓█▄   ▌▒██   ██░▓▓█  ░██░▒██    ▒██     ▓██▒ 
  ▒██▒ ░ ░ ████▓▒░▒▒█████▓    ░▒████▓ ░ ████▓▒░▒▒█████▓ ▒██▒   ░██▒    ▒▄▄  
  ▒ ░░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░    ░▀▀▒ 
    ░      ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ░  ░      ░    ░  ░ 
  ░      ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░ ░ ░ ░ ▒   ░░░ ░ ░ ░      ░          ░ 
             ░ ░     ░           ░        ░ ░     ░            ░       ░    
                               ░                
                    ---===[Author: @MsterHuj]===---
                          --==[Ver : 1.4]==--
'''


@click.group()
def cli_scanner():
    pass


@click.group()
def cli_attack():
    pass


@cli_scanner.command()
@click.option('--ip', type=iptools.IpRangeList, help='ip range to scan with cidr')
@click.option('--timeout', default=1, help='timeout for connection (default 1)')
@click.option('--scan-private', 'scan_private', is_flag=True, type=bool, help='skip private ip for scan')
@click.option('--memcached', is_flag=True, type=bool, help='enable scan for memcached protocol')
@click.option('--ntp', is_flag=True, type=bool, help='enable scan for ntp protocol')
@click.option('--dns', is_flag=True, type=bool, help='enable scan for dns protocol')
@click.option('--all-type', 'all_type', is_flag=True, type=bool, help='enable all scan protocol (memcached, ntp, dns')
@click.option('--output', help='output file')
@click.option('--verbose', is_flag=True, type=bool, help='verbose scan information (show passed ip or other error)')
@click.option('--threads', default=1, help='number of thread for scanner WARN [WIP]')
def scanner(ip, timeout, scan_private, memcached, ntp, dns, all_type, output, verbose, threads):
    """
        Scanner for detect udp port on memcached, dns and ntp
    """

    # check is no dev arg is used
    if ntp:
        print("[*] Error --ntp is not supported for the moment im working on it")
        exit(-1)
    if dns:
        print("[*] Error --dns is not supported for the moment im working on it")
        exit(-1)

    # check if type scan is set
    if not memcached and not ntp and not dns and not all_type:
        print("[*] Error : no type scan specified")
        exit(-1)
    else:

        # todo generate type scan on var scan_used
        if memcached:
            scan_used.append("memcached")
        if dns:
            scan_used.append("dns")
        if ntp:
            scan_used.append("ntp")

        # check if ip is set
        if ip is not None:

            # all right print configuration for scan and run it
            print("-"*40)
            print("Ip to scan       : (error on parse WIP)")  # todo
            print("Scan mod used    : " + str(scan_used))          # todo
            print("Timeout          : " + str(timeout))
            print("Threads          : " + str(threads))
            print("Scan private ip  : " + str(scan_private))
            print("Verbose          : " + str(verbose))
            print("-"*40)

            # generate ip list and send it to checker
            ips = ip.__iter__()

            while True:
                try:
                    ip = iptools.next(ips)

                    if ip not in private:
                        processes_manager(ip, timeout, output, verbose, threads)
                    else:
                        if scan_private:
                            processes_manager(ip, timeout, output, verbose, threads)
                        else:
                            if verbose:
                                print("[*] [" + clock() + "] Skipped private ip '" + ip + "'")

                except StopIteration:
                    print("Finish scan ! " + clock())
                    break

        else:
            print("[*] Error no ip specified")
            print("[*] run with --help for get help")
            print("[*] Exiting..." + clock())


@cli_attack.command()
def attack():
    """
        [WIP] i need to finish the scanner before do dev this part :)
        Attack for overwhelm the targeted network with memcached, dns and ntp
        This script part need a ip list on input
    """
    print(
        "[WIP] i need to finish the scanner before do dev this part :)\nAttack for overwhelm the targeted network with memcached, dns and ntp\nThis script part need a ip list on input")


def processes_manager(ip, timeout, output, verbose, thread):
    if thread >= 2:
        processes.append(multiprocessing.Process(target=fs, args=[ip, timeout, output, verbose]).start())

    else:
        fs(ip, timeout, output, verbose)


def fs(ip, timeout, output, verbose):
    if scan.memcache_udp(ip, timeout):
        print("[+] [" + clock() + "] Found ip " + ip + " !")
        if output is not None:
            save(ip, output)
    else:
        if verbose:
            print("[-] [" + clock() + "] Not found ip " + ip + " !")


def save(ip, output):
    with open(output, "a+") as file:
        file.write(ip + "\n")
        file.close()


def clock():
    return str(round(time.time() - time_start)) + "s"


cli = click.CommandCollection(sources=[cli_scanner, cli_attack])

if __name__ == '__main__':
    print(BANNER)
    cli()
