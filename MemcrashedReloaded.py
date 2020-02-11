from function import filemanager
from function import scanner
from function import settings


def main():
    while True:
        print("1. scan a ip or range of ip")
        print("8. settings app")
        print("9. exit app")

        reply = input("MCR $_ " or '0')

        try:
            reply = int(reply)

            if reply == 1:
                input_ip = input("MCR>scan (enter ip or CIDR) $_ " or '127.0.0.1')
                scanner.scan(input_ip)
            elif reply == 8:
                settings.cli()
            elif reply == 9:
                break
        except TypeError:
            print("Invalid Input !")


if __name__ == '__main__':
    filemanager.init()
    main()
    print("End of script")
