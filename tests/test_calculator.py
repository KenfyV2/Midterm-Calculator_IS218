"""
This module contains unit tests for the Calculator class.
"""

import pytest
from app.calculator import Calculator

def test_add():
    """
    Test the add operation of the Calculator class.
    """
    calc = Calculator()
    result = calc.execute_operation('add', 1, 2)
    assert result == 3

def test_subtract():
    """
    Test the subtract operation of the Calculator class.
    """
    calc = Calculator()
    result = calc.execute_operation('subtract', 2, 1)
    assert result == 1

def test_multiply():
    """
    Test the multiply operation of the Calculator class.
    """
    calc = Calculator()
    result = calc.execute_operation('multiply', 2, 3)
    assert result == 6

def test_divide():
    """
    Test the divide operation of the Calculator class.
    """
    calc = Calculator()
    result = calc.execute_operation('divide', 6, 3)
    assert result == 2

def test_divide_by_zero():
    """
    Test the divide operation of the Calculator class for division by zero.
    """
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.execute_operation('divide', 6, 0)

def test_power():
    """
    Test the power operation of the Calculator class.
    """
    calc = Calculator()
    result = calc.execute_operation('power', 2, 3)
    assert result == 8

def test_root():
    """
    Test the root operation of the Calculator class.
    """
    calc = Calculator()
    result = calc.execute_operation('root', 27, 3)
    assert result == 3
    result = calc.execute_operation('root', 16, 2)
    assert result == 4

def test_root_by_zero():
    """
    Test the root operation of the Calculator class for root by zero.
    """
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot take root with zero"):
        calc.execute_operation('root', 27, 0)

def test_get_history():
    """
    Test the get_history method of the Calculator class.
    """
    calc = Calculator()
    calc.execute_operation('add', 1, 2)
    history = calc.get_history()
    assert not history.empty
    assert history.iloc[-1]['operation'] == 'add'
    assert history.iloc[-1]['operand1'] == 1
    assert history.iloc[-1]['operand2'] == 2
    assert history.iloc[-1]['result'] == 3

def test_load_history():
    """
    Test the load_history method of the Calculator class.
    """
    calc = Calculator()
    calc.load_history('non_existent_file.csv')
    assert calc.history.empty

def test_load_history_with_data(tmp_path):
    """
    Test the load_history method of the Calculator class with data.
    """
    # Create a temporary file to store the history
    history_file = tmp_path / "calculator_history.csv"
    calc = Calculator()
    calc.config.calculator_history_file = str(history_file)

    # Add an operation and save it to the file
    calc.execute_operation('add', 1, 2)
    calc.save_operation('add', 1, 2, 3)
    calc.history.to_csv(history_file, index=False)

    # Load the history from the file
    calc.load_history()
    history = calc.get_history()

    assert not history.empty
    assert history.iloc[-1]['operation'] == 'add'
    assert history.iloc[-1]['operand1'] == 1
    assert history.iloc[-1]['operand2'] == 2
    assert history.iloc[-1]['result'] == 3
