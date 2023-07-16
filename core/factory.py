import logging

from core.base_plugin import BasePlugin

logger = logging.getLogger(__name__)

plugins: dict[str, BasePlugin] = {}


def register_plugin(name: str, cls: BasePlugin) -> None:
    plugins[name] = cls
    logger.info("Registered: %s", name)


def get_plugin(name: str) -> BasePlugin:
    return plugins[name]
