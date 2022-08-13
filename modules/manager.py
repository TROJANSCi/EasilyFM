import time
from shutil import move
from typing import Union
from os import listdir
from os.path import expanduser, join, splitext, exists

from core.config import get_configure, BLACKLIST_EXT
from core.all_formats import extension
from core.utills import create_extension_directory, change_settings
from modules.histrory import logging


def monitoring_paths():
    paths = get_configure().get('monitoring_path')

    if not paths:
        paths = [join(expanduser('~'), 'Downloads')]
        change_settings(monitoring_path=join(expanduser('~'), 'Downloads'))

    for path in paths:
        file = listdir(join(path))
        file_movie(file, path)


def extension_checker(ext: str) -> Union[bool, str]:
    for i in extension:
        if ext.lower() in extension.get(i) and ext.lower() not in BLACKLIST_EXT:
            return create_extension_directory(i)
    return False


def file_movie(files: list, path: str):
    if files:
        for file in files:
            ext = splitext(file)
            file_path = extension_checker(ext=ext[-1])
            if file_path:
                try:

                    if not exists(join(file_path, file)):
                        old = join(path, file)
                        new = join(file_path, file)
                        move(old, new)
                        logging.info(f"{old} -> {new}")
                    else:
                        cur = 1
                        name = f"[copy {cur}] {''.join(ext)}"
                        while exists(join(file_path, name)):
                            cur += 1
                            name = f"[copy {cur}] {''.join(ext)}"

                        old = join(path, file)
                        new = join(file_path, name)
                        move(old, new)
                        logging.info(f"{old} -> {new}")

                except PermissionError:
                    return
