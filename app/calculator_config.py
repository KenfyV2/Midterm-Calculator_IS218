"""
This module defines the CalculatorConfig class, which provides configuration
settings for the Calculator class.
"""

import os

class CalculatorConfig:
    """
    Configuration settings for the Calculator class.
    """
    def __init__(self, precision=2, history_enabled=True,
                 calculator_history_file='data/calculator_history.csv'):
        """
        Initialize the CalculatorConfig with optional settings.

        Args:
            precision (int, optional): The number of decimal places for results. Defaults to 2.
            history_enabled (bool, optional): Whether history is enabled. Defaults to True.
            calculator_history_file (str, optional): The file to store calculator history. 
            Defaults to 'data/calculator_history.csv'.
        """
        self.precision = precision
        self.history_enabled = history_enabled
        self.calculator_history_file = calculator_history_file

    def set_precision(self, precision):
        """
        Set the precision for the calculator results.

        Args:
            precision (int): The number of decimal places for results.
        """
        self.precision = precision

    def enable_history(self, enable=True):
        """
        Enable or disable history.

        Args:
            enable (bool, optional): Whether to enable history. Defaults to True.
        """
        self.history_enabled = enable

    def ensure_history_file_exists(self):
        """
        Ensure the history file exists. Create it if it does not exist.
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.calculator_history_file), exist_ok=True)
        # Create the file if it does not exist
        if not os.path.exists(self.calculator_history_file):
            with open(self.calculator_history_file, 'w', encoding='utf-8') as file:
                file.write('operation,operand1,operand2,result\n')  # Write header for CSV

    def __repr__(self):
        """
        Return a string representation of the CalculatorConfig.

        Returns:
            str: A string representation of the CalculatorConfig.
        """
        return (f"CalculatorConfig(precision={self.precision}, "
                f"history_enabled={self.history_enabled}, "
                f"calculator_history_file='{self.calculator_history_file}')")
