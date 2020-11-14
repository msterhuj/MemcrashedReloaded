class Config:
    """
        Contain :
            driver memory dump setup
            scanner setup
            "todo attack setup"
    """

    storing_null_ip: bool

    def __init__(self):
        pass

    def configure(self):  # todo setup configure
        self.storing_null_ip = bool(input("Store ip with all false from scanner ? (default True) " or 1))
        print(str(self.storing_null_ip))