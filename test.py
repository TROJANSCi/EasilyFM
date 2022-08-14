import configparser
import json

config = configparser.ConfigParser()
config.sections()

config.read('settings.ini')


for i in config.sections():

    for j in config[i].values():
        c = json.loads(j)
        print(c, type(c))



