import threading
import time
from os import startfile

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from config import cfg
from managers import file_list_monitor
from utills import _path

status = False


def starting():
    while status:
        file_list_monitor(cfg().get('monitoring_path'))
        time.sleep(5)


def starts():
    global status, start_stop
    if status:
        start_stop.setText("Start")
        start_stop.setIcon(QIcon('ui\\start.png'))
        status = False
    else:
        start_stop.setText("Stop")
        start_stop.setIcon(QIcon('ui\\stop.png'))
        status = True
    thread = threading.Thread(target=starting)
    thread.setDaemon(True)
    thread.start()


def open_dirs():
    startfile(_path())


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

tray = QSystemTrayIcon()
tray.setIcon(QIcon('ui\\icons.png'))
tray.setVisible(True)

menu = QMenu()

start_stop = QAction("Start")
open_dir = QAction("Open folder")
settings = QAction("Settings")
exits = QAction("Quit")

open_dir.setIcon(QIcon('ui\\folder.png'))
start_stop.setIcon(QIcon('ui\\start.png'))
settings.setIcon(QIcon("ui\\settings2.png"))
exits.setIcon(QIcon('ui\\exits.png'))

exits.triggered.connect(app.quit)
open_dir.triggered.connect(open_dirs)
start_stop.triggered.connect(starts)

menu.addAction(start_stop)
menu.addSeparator()
menu.addAction(open_dir)
menu.addSeparator()
menu.addAction(settings)
menu.addSeparator()
menu.addAction(exits)

if __name__ == "__main__":
    tray.setContextMenu(menu)
    tray.setToolTip("Test")

    app.exec()
