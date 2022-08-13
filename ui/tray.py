import time
import threading
from os.path import dirname, abspath, join

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from modules.utils import open_finally_dir, open_history
from modules.manager import monitoring_paths

status = False


def start_monitor():
    while status:
        monitoring_paths()
        time.sleep(5)


def process_monitor():
    global status
    if status:
        process.setText("Start")
        process.setIcon(ico_start)
        status = False
    else:
        process.setText("Stop")
        process.setIcon(ico_stop)
        status = True
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

process = QAction("Start")
open_dir = QAction("Open folder")
open_history_file = QAction("Open history")
settings = QAction("Settings")
exits = QAction("Quit")

open_dir.setIcon(ico_folder)
process.setIcon(ico_start)
open_history_file.setIcon(ico_history)
settings.setIcon(ico_settings2)
exits.setIcon(ico_exits)

exits.triggered.connect(app.quit)
open_dir.triggered.connect(open_finally_dir)
process.triggered.connect(process_monitor)
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
tray.setToolTip("Test")