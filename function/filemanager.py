import os
from function.settings import Settings


def init():
    if not os.path.isdir("./data"):
        print("Data Directory do not exist lets create it !")
        os.mkdir("data")

    if not os.path.exists("./data/settings.json"):
        print("Settings file dose exist !")
        param = Settings()
        param.save()


def save_ip(result, ip):
    if result:
        with open("./data/valid-ip.txt", "a+") as file:
            print("Valid ip : " + ip)
            file.write(ip + "\n")
            file.close()
    else:
        print("Nop ip : " + ip)
