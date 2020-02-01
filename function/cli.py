from function import scanner
from function.cli_commands import settings as fun_settings

def run():
    cli = True
    while cli:
        banner()
        exe(input("MCR $_ " or '0'))


def banner():
    print("1. scan a ip or range of ip")
    print("8. settings app")
    print("9. exit app")


def exe(reply):
    try:
        reply = int(reply)

        if reply == 1:
            input_ip = input("MCR>scan $_ " or '127.0.0.1')
            scanner.scan(input_ip)
        elif reply == 8:
            fun_settings.main()
        elif reply == 9:
            exit(0)
    except TypeError:
        print("Invalid Input !")