from function.settings import Settings
from function import settings

param = settings.load()


def banner():
    print()


def show_config():
    print("Setting:")
    print("Ping before test host: " + str(param.isPing))


def main():
    show_config()


show_config()
