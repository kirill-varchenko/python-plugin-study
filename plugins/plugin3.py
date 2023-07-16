import logging

logger = logging.getLogger(__name__)

logger.info("Loaded")


# Not loaded because doesn't inherit BasePlugin
class Plugin3:
    ...
