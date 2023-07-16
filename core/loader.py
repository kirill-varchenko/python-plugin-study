import importlib
import inspect
import logging
from pathlib import Path
from typing import Any, Callable

from core.base_plugin import BasePlugin
from core.factory import register_plugin

logger = logging.getLogger(__name__)


def is_plugin_in_module(module_name: str) -> Callable[[Any], bool]:
    def is_plugin(obj: Any) -> bool:
        return (
            inspect.isclass(obj)
            and obj.__module__ == module_name
            and issubclass(obj, BasePlugin)
        )

    return is_plugin


def load_plugins_from_folder(plugin_folder: str) -> None:
    for python_file in Path(plugin_folder).glob("*.py"):
        module_name = f"{plugin_folder}.{python_file.with_suffix('').name}"
        module = importlib.import_module(module_name)
        logger.info("Imported %s", module)
        for obj_name, obj in inspect.getmembers(
            module, is_plugin_in_module(module_name)
        ):
            register_plugin(obj_name, obj)
