import json
from os.path import join, isfile, realpath, dirname

APP_DIR = dirname(realpath(__file__))
SETTINGS = join(APP_DIR, 'settings.json')
DIRNAME = join(APP_DIR, 'dirname.json')
DICTIONARY = join(APP_DIR, 'language.json')


def rollback():
    resource = join(APP_DIR, 'resource')

    if isfile(resource) and not isfile(SETTINGS) or not isfile(DIRNAME) or not isfile(DICTIONARY):

        try:
            with open(resource, 'r', encoding='utf-8') as file:
                conf: dict = json.loads(file.read())

                if not isfile(SETTINGS):
                    settings = open(SETTINGS, 'w', encoding='utf-8')
                    json.dump(conf.get('settings'), settings, ensure_ascii=False, indent=4)
                    settings.close()

                if not isfile(DIRNAME):
                    name = open(DIRNAME, 'w', encoding='utf-8')
                    json.dump(conf.get('dirname'), name, ensure_ascii=False, indent=4)
                    name.close()

                if not isfile(DICTIONARY):
                    dicts = open(DICTIONARY, 'w', encoding='utf-8')
                    json.dump(conf.get('language'), dicts, ensure_ascii=False, indent=4)
                    dicts.close()

        finally:
            file.close()


