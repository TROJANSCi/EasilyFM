import json
from os import name
from os.path import join, dirname, abspath

s = '\\' if name == 'nt' else '/'
APP_DIR = join(dirname(abspath(__file__)), f"..{s}")
SETTINGS = join(APP_DIR, 'settings.json')
DICTIONARY = join(APP_DIR, 'language.json')
DIRNAME = join(APP_DIR, "dirname.json")
SUPPORTED_LANGUAGES = ['ar', 'ru', 'uz', 'zh', 'de', 'fr', 'uk', 'be', 'da',
                       'es', 'et', 'fi', 'ga', 'hi', 'it', 'ja', 'ko', 'pl']


def get_configure() -> dict:
    file = open(SETTINGS, 'r', encoding='utf-8')
    configure = json.load(file)
    return configure


def get_dict(word: str = None, library: str = DICTIONARY) -> str:
    lang = get_configure().get('language')
    file = open(library, 'r', encoding='utf-8')
    dicts = json.load(file)
    if lang and lang in SUPPORTED_LANGUAGES:
        return dicts.get(lang).get(word)

    return dicts.get('en').get(word)


BLACKLIST_EXT = get_configure().get('black_list_ext')
BLACKLIST_FILES = get_configure().get('black_list_files')
