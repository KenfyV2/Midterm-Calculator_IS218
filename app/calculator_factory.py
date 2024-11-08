"""
This module provides a factory for creating different types of calculators.
"""

from app.calculator import Calculator

class CalculatorFactory:
    """
    The CalculatorFactory class provides a factory method for creating calculators.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    @staticmethod
    def create_calculator():
        """
        Create and return a new Calculator instance.
        """
        return Calculator()
