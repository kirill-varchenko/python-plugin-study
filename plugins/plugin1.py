import logging

from core.base_plugin import BasePlugin

logger = logging.getLogger(__name__)

logger.info("Loaded")


class Plugin1(BasePlugin):
    ...
