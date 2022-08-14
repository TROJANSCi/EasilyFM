from os import startfile
from os.path import join
from core.utills import check_finally_path
from core.config import APP_DIR


def open_finally_dir():
    startfile(check_finally_path())


def open_history():
    startfile(join(APP_DIR, "history.txt"))


def open_settings():
    startfile(join(join(APP_DIR, 'core'), 'settings.json'))
