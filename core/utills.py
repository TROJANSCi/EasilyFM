import hjson
from os import makedirs
from os.path import expanduser, join, isdir

from core.config import set_file, get_configure


def check_finally_path() -> str:

    if get_configure().get('finally_path'):
        finally_path = get_configure().get('finally_path')

    else:
        finally_path = expanduser('~')
        change_settings(finally_path=expanduser('~'))

    if get_configure().get('finally_dir'):
        finally_dir = get_configure().get('finally_dir')

    else:
        finally_dir = "Downloads"
        change_settings(finally_dir="Downloads")

    path = join(finally_path, finally_dir)

    if isdir(path):
        return path

    new_path = join(expanduser('~'), 'Downloads')
    makedirs(new_path, exist_ok=True)
    return new_path


def change_settings(**kwargs):
    with open(set_file, 'r+') as f:
        h = hjson.load(f)
        print(h)
    #     data = hjson.load(f)
    #     for j in kwargs:
    #         data[j] = kwargs[j] if j != 'monitoring_path' else [kwargs[j]]
    #         f.seek(0)
    #         hjson.dump(data, f, indent=4, ensure_ascii=False)
    #         f.truncate()
    # f.close()
    # return kwargs.get(str(*kwargs))


def create_extension_directory(ext: str, finally_dir: str = check_finally_path()) -> str:
    name = f"#{ext.title()}"
    path = join(finally_dir, name)
    makedirs(path, exist_ok=True)
    return path
