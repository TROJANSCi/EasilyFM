import json
from os import name
from os.path import join, dirname, abspath

s = '\\' if name == 'nt' else '/'
APP_DIR = join(dirname(abspath(__file__)), f"..{s}")
SETTINGS = join(APP_DIR, 'settings.json')


def get_configure() -> dict:
    file = open(SETTINGS, 'r', encoding='utf-8')
    configure = json.load(file)
    return configure


BLACKLIST_EXT = get_configure().get('black_list_ext')
BLACKLIST_FILES = get_configure().get('black_list_files')
