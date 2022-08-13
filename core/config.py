import json
from os.path import join, dirname

path = join(dirname(__file__), 'settings.json')


def get_configure():
    file = open(path, 'r', encoding='utf-8')
    configure = json.load(file)
    return configure
