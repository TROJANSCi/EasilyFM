from rollback import rollback; rollback()
from modules.histrory import logging
from ui.tray import app


__version__ = 0.1
__author__ = "TROJASNCi"
__company__ = "LOGITE SOFT"

if __name__ == "__main__":
    logging.info("Starting")
    app.exec()
