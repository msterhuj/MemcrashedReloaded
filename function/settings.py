import jsonpickle as json


def load():
    with open("./data/settings.json", "r") as file:
        data = file.read().replace('\n', '')
        return json.decode(data)


class Settings:
    def __init__(self):
        self.ping = True
        self.chat = "black"

    def save(self):
        with open("./data/settings.json", "w+") as file:
            file.write(json.encode(self))
            file.close()

    # Getter And Setter
    def isPing(self):
        return self.ping

    def setPing(self, o):
        self.ping = o
