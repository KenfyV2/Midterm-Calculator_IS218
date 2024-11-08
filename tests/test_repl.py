"""
This module contains tests for the REPL class.
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
    assert 'exit' in repl.commands

def test_add_command(monkeypatch):
    """
    Test the add command in the REPL.
    """
    repl = REPL()
    inputs = iter(['add', '1', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    assert repl.calculator.history.iloc[-1]['result'] == 3

def test_subtract_command(monkeypatch):
    """
    Test the subtract command in the REPL.
    """
    repl = REPL()
    inputs = iter(['subtract', '5', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    assert repl.calculator.history.iloc[-1]['result'] == 2

def test_multiply_command(monkeypatch):
    """
    Test the multiply command in the REPL.
    """
    repl = REPL()
    inputs = iter(['multiply', '2', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
    assert repl.calculator.history.iloc[-1]['result'] == 6

def test_divide_command(monkeypatch):
    """
    Test the divide command in the REPL.
    """
    repl = REPL()
    inputs = iter(['divide', '6', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
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
    assert repl.calculator.history.empty

def test_unknown_command(monkeypatch):
    """
    Test the REPL with an unknown command.
    """
    repl = REPL()
    inputs = iter(['unknown', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: None)
    with pytest.raises(SystemExit):
        repl.run()
