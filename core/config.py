import json
from os.path import join, dirname, abspath
from os import name

splash = "\\" if name == 'nt' else '/'
APP_DIR = join(dirname(abspath(__file__)), f"..{splash}")

set_file = join(dirname(__file__), 'settings.json')



def get_configure() -> dict:
    file = open(set_file, 'r', encoding='utf-8')
    configure = json.load(file)
    return configure


BLACKLIST_EXT = get_configure().get('black_list_ext')
BLACKLIST_FILES = get_configure().get('black_list_files')
