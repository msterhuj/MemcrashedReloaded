import jsonpickle as json


def cli():

    option = load()

    while True:
        print("1. Show current settings")
        print("9. quit and save settings")

        reply = input("MCR>Settings $_ " or '0')

        try:
            reply = int(reply)

            if reply == 1:
                print("")
            elif reply == 9:
                option.save()
                break
        except TypeError:
            print("Invalid Input !")


def load():
    with open("./data/settings.json", "r") as file:
        data = file.read().replace('\n', '')
        return json.decode(data)


class Settings:
    def __init__(self):
        self.timeOut = 1  # time out for scanner connect
        self.skipPrivate = False  # Skip private ip when scan running

    def save(self):
        with open("./data/settings.json", "w+") as file:
            file.write(json.encode(self))
            file.close()

    # Getter And Setter

    def getTimeOut(self):
        return self.timeOut

    def setTimeOut(self, i):
        self.timeOut = i

    def skipPrivate(self):
        return self.skipPrivate

    def setSkipPrivate(self, i):
        self.setSkipPrivate(i)
