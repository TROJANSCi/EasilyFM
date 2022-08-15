import threading
import time
from os.path import dirname, abspath, join

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from core.config import get_dict
from modules.manager import monitoring_paths
from modules.utils import open_finally_dir, open_history, open_settings

status = False


def start_monitor():
    while status:
        monitoring_paths()
        time.sleep(0.5)


def process_monitor():
    global status
    if status:
        process.setText(get_dict('start'))
        process.setIcon(ico_start)
        status = False
        tray.setToolTip("└► Easily File manager - stopped.")

    else:
        process.setText(get_dict('stop'))
        process.setIcon(ico_stop)
        status = True
        tray.setToolTip("└► Easily File manager - started.")

    thread = threading.Thread(target=start_monitor)
    thread.setDaemon(True)
    thread.start()


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

ico_folder = QIcon(join(dirname(abspath(__file__)), "folder.png"))
ico_start = QIcon(join(dirname(abspath(__file__)), "start.png"))
ico_stop = QIcon(join(dirname(abspath(__file__)), "stop.png"))
ico_settings2 = QIcon(join(dirname(abspath(__file__)), "settings2.png"))
ico_exits = QIcon(join(dirname(abspath(__file__)), "exits.png"))
ico_icons = QIcon(join(dirname(abspath(__file__)), "icons.png"))
ico_history = QIcon(join(dirname(abspath(__file__)), "history.png"))

tray = QSystemTrayIcon()
tray.setIcon(ico_icons)
tray.setVisible(True)

menu = QMenu()

process = QAction(get_dict('start'))
open_dir = QAction(get_dict('folder'))
open_history_file = QAction(get_dict('history'))
settings = QAction(get_dict('settings'))
exits = QAction(get_dict('exit'))

open_dir.setIcon(ico_folder)
process.setIcon(ico_start)
open_history_file.setIcon(ico_history)
settings.setIcon(ico_settings2)
exits.setIcon(ico_exits)

exits.triggered.connect(app.quit)
open_dir.triggered.connect(open_finally_dir)
process.triggered.connect(process_monitor)
settings.triggered.connect(open_settings)
open_history_file.triggered.connect(open_history)

menu.addAction(process)
menu.addSeparator()
menu.addAction(open_dir)
menu.addAction(open_history_file)
menu.addSeparator()
menu.addAction(settings)
menu.addSeparator()
menu.addAction(exits)

tray.setContextMenu(menu)
tray.setToolTip("└► Easily File manager - stopped.")
