"""
This module contains unit tests for the REPL class.
"""

import pytest
from app.repl import REPL

def test_repl_commands():
    """
    Test that the REPL initializes with the correct commands.
    """
    repl = REPL()
    assert 'add' in repl.commands
    assert 'subtract' in repl.commands
    assert 'multiply' in repl.commands
    assert 'divide' in repl.commands
    assert 'power' in repl.commands
    assert 'root' in repl.commands
    assert 'history' in repl.commands
    assert 'clear' in repl.commands
    assert 'save' in repl.commands
    assert 'load' in repl.commands
    assert 'menu' in repl.commands
    assert 'exit' in repl.commands

def test_add_command(monkeypatch):
    """
    Test the add command in the REPL.
    """
    repl = REPL()
    inputs = iter(['add', '1', '1', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    assert not repl.calculator.history.empty
    assert repl.calculator.history.iloc[-1]['result'] == 2

def test_divide_by_zero_command(monkeypatch):
    """
    Test the divide command in the REPL for division by zero.
    """
    repl = REPL()
    inputs = iter(['divide', '6', '0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        repl.calculator.execute_operation('divide', 6, 0)

def test_unknown_command(monkeypatch):
    """
    Test the REPL with an unknown command.
    """
    repl = REPL()
    inputs = iter(['unknown', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    printed = []
    monkeypatch.setattr('builtins.print', printed.append)
    with pytest.raises(SystemExit):
        repl.run()
    assert "Unknown command" in printed

def test_clear_history_command(monkeypatch):
    """
    Test the clear history command in the REPL.
    """
    repl = REPL()
    inputs = iter(['add', '1', '1', 'clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    assert repl.calculator.history.empty

def test_save_history_command(monkeypatch):
    """
    Test the save history command in the REPL.
    """
    repl = REPL()
    inputs = iter(['add', '1', '1', 'save', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    assert not repl.calculator.history.empty

def test_load_history_command(monkeypatch):
    """
    Test the load history command in the REPL.
    """
    repl = REPL()
    inputs = iter(['load', 'calculator_history.csv', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    assert not repl.calculator.history.empty

def test_menu_command(monkeypatch):
    """
    Test the menu command in the REPL.
    """
    repl = REPL()
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    printed = []
    monkeypatch.setattr('builtins.print', printed.append)
    with pytest.raises(SystemExit):
        repl.run()
    assert "Available commands:" in printed

def test_exit_command(monkeypatch):
    """
    Test the exit command in the REPL.
    """
    repl = REPL()
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.run()

def test_load_plugins(monkeypatch):
    """
    Test loading plugins in the REPL.
    """
    repl = REPL()
    monkeypatch.setattr('os.listdir', lambda _: ['add.py', 'subtract.py'])

    class MockSpec:
        """
        A mock spec class for testing.
        """
        def __init__(self):
            self.loader = self
        def exec_module(self, module):
            """
            Mock exec_module method.
            """
            setattr(module, 'add', lambda a, b: a + b)
            setattr(module, 'subtract', lambda a, b: a - b)
        def load_module(self, _):
            """
            Mock load_module method.
            """
            return None

    monkeypatch.setattr('importlib.util.spec_from_file_location', lambda name, path: MockSpec())
    monkeypatch.setattr('importlib.util.module_from_spec', lambda spec: spec)

    repl.load_plugins()
    assert 'add' in repl.commands
    assert 'subtract' in repl.commands
