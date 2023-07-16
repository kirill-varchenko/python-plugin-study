import logging

from core.loader import load_plugins_from_folder

logging.basicConfig(format="%(asctime)s %(module)10s %(message)s", level=logging.INFO)

load_plugins_from_folder("plugins")
