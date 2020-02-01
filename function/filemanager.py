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