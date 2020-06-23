from pathlib import Path


class Data:
    def __init__(self, all_in_one=False, filename="ips"):
        self.all_in_one = all_in_one
        self.filename = filename
        Path("data").mkdir(parents=True, exist_ok=True)

    def set_properties(self, all_in_one, filename):
        self.all_in_one = all_in_one
        self.filename = filename

    def save(self, ip, saver="service_name"):
        if self.all_in_one:
            with open("./data/" + self.filename + ".txt", "a+") as file:
                file.write(ip + "\n")
                file.close()
        else:
            with open("./data/ips_" + saver + ".txt", "a+") as file:
                file.write(ip + "\n")
                file.close()
