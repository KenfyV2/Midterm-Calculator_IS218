"""
This module provides functionality to load plugins dynamically.
"""

import importlib
import pkgutil

def load_plugins():
    """
    Load plugins dynamically from the current package.

    Returns:
        dict: A dictionary of plugin names and their corresponding callable objects.
    """
    plugins = {}
    package = __package__
    for _, name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"{package}.{name}")
        for attr in dir(module):
            if callable(getattr(module, attr)):
                plugins[attr] = getattr(module, attr)
    return plugins
