"""
This module contains unit tests for the plugins.
"""

import pytest
from app.plugins.add import add
from app.plugins.subtract import subtract
from app.plugins.multiply import multiply
from app.plugins.divide import divide
from app.plugins.power import power
from app.plugins.root import root

def test_add():
    """
    Test the add plugin.
    """
    assert add(1, 2) == 3

def test_subtract():
    """
    Test the subtract plugin.
    """
    assert subtract(2, 1) == 1

def test_multiply():
    """
    Test the multiply plugin.
    """
    assert multiply(2, 3) == 6

def test_divide():
    """
    Test the divide plugin.
    """
    assert divide(6, 3) == 2

def test_divide_by_zero():
    """
    Test the divide plugin for division by zero.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(6, 0)

def test_power():
    """
    Test the power plugin.
    """
    assert power(2, 3) == 8

def test_root():
    """
    Test the root plugin.
    """
    assert root(27, 3) == 3
    assert root(16, 2) == 4

def test_root_by_zero():
    """
    Test the root plugin for root by zero.
    """
    with pytest.raises(ValueError, match="Cannot take root with zero"):
        root(27, 0)
