"""
This module contains tests for the Calculator class.
"""

import pytest
from app.calculator import Calculator

def test_add():
    """
    Test the add method of the Calculator class.
    """
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    """
    Test the subtract method of the Calculator class.
    """
    calc = Calculator()
    assert calc.subtract(2, 1) == 1

def test_multiply():
    """
    Test the multiply method of the Calculator class.
    """
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    """
    Test the divide method of the Calculator class.
    """
    calc = Calculator()
    assert calc.divide(6, 3) == 2

def test_divide_by_zero():
    """
    Test the divide method of the Calculator class for division by zero.
    """
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(6, 0)
