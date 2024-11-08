"""
This module contains tests for the App class.
"""

import pytest
from app.app import App

def test_app_initialization():
    """
    Test that the App initializes with a REPL instance.
    """
    app = App()
    assert app.repl is not None

def test_app_run(monkeypatch):
    """
    Test that the App runs the REPL and exits correctly.
    """
    app = App()
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        app.run()
