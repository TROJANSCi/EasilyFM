import os
from random import randint
from shutil import move

from _formats import extension
from utills import _path, black_list_ext, black_list_file


def find_extension(ext):
    for i in extension:
        if ext in extension.get(i) and ext not in black_list_ext:
            return _path(i)
    return False


def file_list_monitor(path):
    for j in path:
        files = os.listdir(os.path.join(j))
        splash = "\\" if os.name == 'nt' else '/'
        for file in files:
            ext = os.path.splitext(file)[-1]
            check = find_extension(ext)
            if check and file not in black_list_file:
                try:
                    if os.path.exists(os.path.join(check, file)):
                        move(j + splash + file, f"{check}[copy-{randint(10000, 99999)}]_{file}")
                    else:
                        move(j + splash + file, check)
                except PermissionError:
                    return
