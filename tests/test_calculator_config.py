"""
This module contains unit tests for the CalculatorConfig class.
"""

from unittest.mock import patch, mock_open
from app.calculator_config import CalculatorConfig

def test_default_config():
    """
    Test the default configuration of the CalculatorConfig class.
    """
    with patch('os.makedirs'), patch('builtins.open', mock_open()):
        config = CalculatorConfig()
        assert config.precision == 2
        assert config.history_enabled
        assert config.calculator_history_file == 'data/calculator_history.csv'

def test_set_precision():
    """
    Test the set_precision method of the CalculatorConfig class.
    """
    with patch('os.makedirs'), patch('builtins.open', mock_open()):
        config = CalculatorConfig()
        config.set_precision(5)
        assert config.precision == 5

def test_enable_history():
    """
    Test the enable_history method of the CalculatorConfig class.
    """
    with patch('os.makedirs'), patch('builtins.open', mock_open()):
        config = CalculatorConfig()
        config.enable_history(False)
        assert not config.history_enabled

def test_ensure_history_file_exists():
    """
    Test the ensure_history_file_exists method of the CalculatorConfig class.
    """
    with patch('os.makedirs') as mock_makedirs, patch('builtins.open', mock_open()) as mock_file:
        config = CalculatorConfig()
        config.ensure_history_file_exists()
        mock_makedirs.assert_called_once_with('data', exist_ok=True)
        mock_file.assert_called_once_with('data/calculator_history.csv', 'w', encoding='utf-8')

def test_repr():
    """
    Test the __repr__ method of the CalculatorConfig class.
    """
    with patch('os.makedirs'), patch('builtins.open', mock_open()):
        config = CalculatorConfig()
        expected_repr = ("CalculatorConfig(precision=2, history_enabled=True, "
                         "calculator_history_file='data/calculator_history.csv')")
        assert repr(config) == expected_repr

def test_custom_config():
    """
    Test custom configuration of the CalculatorConfig class.
    """
    with patch('os.makedirs'), patch('builtins.open', mock_open()):
        config = CalculatorConfig(precision=4, history_enabled=False,
                                  calculator_history_file='custom_history.csv')
        assert config.precision == 4
        assert not config.history_enabled
        assert config.calculator_history_file == 'custom_history.csv'
