"""
This module contains tests for the plugin functions.
"""

import pytest
from app.plugins.add import add_command as add
from app.plugins.subtract import subtract_command as subtract
from app.plugins.multiply import multiply_command as multiply
from app.plugins.divide import divide_command as divide

def test_add():
    """
    Test the add_command function.
    """
    assert add(1, 2) == 3

def test_subtract():
    """
    Test the subtract_command function.
    """
    assert subtract(2, 1) == 1

def test_multiply():
    """
    Test the multiply_command function.
    """
    assert multiply(2, 3) == 6

def test_divide():
    """
    Test the divide_command function.
    """
    assert divide(6, 3) == 2

def test_divide_by_zero():
    """
    Test the divide_command function for division by zero.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(6, 0)
