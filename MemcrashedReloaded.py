import click
import iptools
import socket
import time
import multiprocessing

processes = []
time_start = time.time()

private = iptools.IpRangeList(
    '0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24', '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4', '240.0.0.0/4', '255.255.255.255/32'
)


@click.command()
@click.option('--ip', help='ip range to scan with cidr', type=iptools.IpRangeList)
@click.option('--timeout', default=1, help='timeout for connection (default 1)')
@click.option('--scan-private', 'scan_private', is_flag=True, type=bool, help='skip private ip for scan')
@click.option('--output', help='output file')
@click.option('--verbose', is_flag=True, type=bool, help='verbose scan information (show passed ip or other error)')
@click.option('--thread', default=1, help='number of thread for scanner WARN the number of scanner not work for the moment if is set to over 1 the scanner generate many thread you need a good pc ;)')
def main(ip, timeout, scan_private, output, verbose, thread):
    """
    Scanner version 1.3.\n
    Latest change : Full rewrite command manager.\n
    Creator : @MsterHuj.\n
    !\ I am not responsible for any damages caused by using this tool. /!\
    """
    if ip is not None:

        # generate ip list and send it to checker
        ips = ip.__iter__()

        while True:
            try:
                ip = iptools.next(ips)

                if ip not in private:
                    processes_manager(ip, timeout, output, verbose, thread)
                else:
                    if scan_private:
                        processes_manager(ip, timeout, output, verbose, thread)
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


if __name__ == '__main__':
    print("Working on version 2.0 on TouDom.py")
    main()
