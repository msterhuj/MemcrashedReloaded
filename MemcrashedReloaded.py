from function import filemanager
from function import cli
from function.settings import Settings
from function import settings

settings = settings.load()
filemanager.init()
cli.run()
