import json

class Data:
    name: str = "File data format .json"
    description = "Store ip information"
    author = "@MsterHuj"

    data_file = "./data.json"
    file = None
    data = ""

    def __init__(self):
        self.file = open(self.data_file, "w")
        pass

    def load(self):
        pass

    def save(self, data: list):
        json.load()
        pass
