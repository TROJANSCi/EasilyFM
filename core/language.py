from core.config import get_configure

dicts = {
    'en': {
        'start': 'Start',
        'stop': 'Stop',
        'folder': 'Open destination folder',
        'history': 'History',
        'settings': 'Settings',
        'exit': 'Exit'
    },
    'ru': {
        'start': 'Старт',
        'stop': 'Остановить',
        'folder': 'Открыть папку назначения',
        'history': 'История',
        'settings': 'Настройки',
        'exit': 'Выход'

    },
    'uz': {
        'start': 'Start',
        'stop': 'Stop',
        'folder': 'Belgilangan papkani oching',
        'history': 'Tarix',
        'settings': 'Sozlamalar',
        'exit': 'Chiqish'

    },
    'zh': {
        'start': '开始',
        'stop': '停止',
        'folder': '打开目标文件夹',
        'history': '历史',
        'settings': '设置',
        'exit': '出口'

    }
}


def dictionary(key: str) -> str:
    _ = get_configure().get('language')
    return dicts[_.lower()].get(key)
