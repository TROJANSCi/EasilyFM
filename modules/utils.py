from os.path import join

from startfile import startfile

from core.config import APP_DIR
from core.utills import check_finally_path


def open_finally_dir():
    startfile(check_finally_path())


def open_history():
    startfile(join(APP_DIR, "history.txt"))


def open_settings():
    startfile(join(APP_DIR, 'settings.json'))
