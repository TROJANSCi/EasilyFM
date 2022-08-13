import logging
from os.path import join

from core.config import APP_DIR

logging.basicConfig(filename=join(APP_DIR, f"history.txt"),
                    level=logging.INFO,
                    format="%(asctime)s %(message)s")
