"""
This module defines strategy classes for different arithmetic operations.
"""

from abc import ABC, abstractmethod

class OperationStrategy(ABC):
    """
    Abstract base class for operation strategies.
    """
    @abstractmethod
    def execute(self, a, b):
        """
        Execute the operation strategy.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the operation.
        """
        # No need for pass here since it's an abstract method

class AddStrategy(OperationStrategy):
    """
    Strategy class for addition.
    """
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Execute the addition strategy.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the addition.
        """
        return a + b

class SubtractStrategy(OperationStrategy):
    """
    Strategy class for subtraction.
    """
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Execute the subtraction strategy.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the subtraction.
        """
        return a - b

class MultiplyStrategy(OperationStrategy):
    """
    Strategy class for multiplication.
    """
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Execute the multiplication strategy.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the multiplication.
        """
        return a * b

class DivideStrategy(OperationStrategy):
    """
    Strategy class for division.
    """
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Execute the division strategy.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the division.

        Raises:
            ValueError: If the second operand is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class PowerStrategy(OperationStrategy):
    """
    Strategy class for exponentiation.
    """
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Execute the exponentiation strategy.

        Args:
            a (float): The base.
            b (float): The exponent.

        Returns:
            float: The result of the exponentiation.
        """
        return a ** b

class RootStrategy(OperationStrategy):
    """
    Strategy class for root calculation.
    """
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Execute the root calculation strategy.

        Args:
            a (float): The number.
            b (float): The root.

        Returns:
            float: The result of the root calculation.

        Raises:
            ValueError: If the root is zero.
        """
        if b == 0:
            raise ValueError("Cannot take root with zero")
        return a ** (1 / b)
