"""
This module contains tests for the plugin loading functionality.
"""

from app.plugins import load_plugins

def test_load_plugins():
    """
    Test that the load_plugins function loads all expected plugins.
    """
    plugins = load_plugins()
    assert 'add' in plugins
    assert 'subtract' in plugins
    assert 'multiply' in plugins
    assert 'divide' in plugins
    assert 'power' in plugins
    assert 'root' in plugins
