"""
This module provides functionality to dynamically load plugins for the calculator application.
"""

import importlib
import os

def load_plugins():
    """
    Load and return a dictionary of plugin commands.

    This function dynamically loads all Python modules in the current directory
    (excluding __init__.py) and retrieves a command function from each module.

    Returns:
        dict: A dictionary where the keys are the plugin names and the values are the command 
        functions.
    """
    plugins = {}
    plugin_dir = os.path.dirname(__file__)
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module = importlib.import_module(f'app.plugins.{module_name}')
            command_name = f"{module_name}_command"
            plugins[module_name] = getattr(module, command_name)
    return plugins
