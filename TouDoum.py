import click
import iptools
import socket
import time
import multiprocessing

time_start = time.time()
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
@click.option('--threads', default=1,
              help='number of thread for scanner WARN the number of scanner not work for the moment if is set to over 1 the scanner generate many thread you need a good pc ;)')
def scanner(ip, timeout, scan_private, memcached, ntp, dns, all_type, output, verbose, threads):
    """
        Scanner for detect udp port on memcached, dns and ntp
    """
    if ip is not None:

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
    print("[WIP] i need to finish the scanner before do dev this part :)\nAttack for overwhelm the targeted network with memcached, dns and ntp\nThis script part need a ip list on input")


def processes_manager(ip, timeout, output, verbose, thread):
    if thread >= 2:
        processes.append(multiprocessing.Process(target=scan, args=[ip, timeout, output, verbose]).start())

    else:
        scan(ip, timeout, output, verbose)


def scan(ip, timeout, output, verbose):
    if check_memcached(ip, timeout):
        print("[+] [" + clock() + "] Found ip " + ip + " !")
        if output is not None:
            save(ip, output)
    else:
        if verbose:
            print("[-] [" + clock() + "] Not found ip " + ip + " !")


def check_memcached(ip, time_out):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(time_out)
        soc.connect((ip, 11211))
        soc.shutdown(2)
        return True
    except socket.timeout:
        return False
    except OSError:
        return False
    except ConnectionRefusedError:
        return False
    except KeyboardInterrupt:
        print("[*] Exiting..." + clock())
        exit()


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
