import json
import os

from config import cfg

splash = "\\" if os.name == 'nt' else '/'


def _change_settings(**kwargs):
    with open('core/settings.json', 'r+') as f:
        data = json.load(f)
        for j in kwargs:
            data[j] = kwargs[j] if j != 'monitoring_path' else [kwargs[j]]
            f.seek(0)
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()
    f.close()
    return kwargs.get(str(*kwargs))


def _check_dirs():
    home = os.path.expanduser('~')
    main_dir = cfg()['finally_dir'] if cfg()['finally_dir'] else _change_settings(finally_dir="Downloads")
    cfg()['monitoring_path'] if cfg()['monitoring_path'] else _change_settings(
        monitoring_path=f'{home}{splash}{main_dir}')
    cfg()['finally_path'] if cfg()['finally_path'] else _change_settings(finally_path=home)


def _path(_ext=None):
    _check_dirs()
    f_path = cfg()['finally_path']
    m_dir = cfg()['finally_dir']
    if _ext:
        path = f"{f_path}{splash}{m_dir}{splash}#{_ext.title()}{splash}"
        os.makedirs(path, exist_ok=True)
    else:
        path = f"{f_path}{splash}{m_dir}"

    return path


black_list_file = cfg().get('black_list_file')
black_list_ext = cfg().get('black_list_ext')
