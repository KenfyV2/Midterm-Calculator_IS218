"""
This module provides strategy classes for different arithmetic operations.
"""

class OperationStrategy:
    """
    The OperationStrategy class defines the interface for arithmetic operations.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Execute the operation with the given operands.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the operation.
        """
        raise NotImplementedError("You should implement this method.")

class AddStrategy(OperationStrategy):
    """
    The AddStrategy class implements the addition operation.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Perform addition of two numbers.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of adding a and b.
        """
        return a + b

class SubtractStrategy(OperationStrategy):
    """
    The SubtractStrategy class implements the subtraction operation.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Perform subtraction of two numbers.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of subtracting b from a.
        """
        return a - b

class MultiplyStrategy(OperationStrategy):
    """
    The MultiplyStrategy class implements the multiplication operation.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Perform multiplication of two numbers.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of multiplying a and b.
        """
        return a * b

class DivideStrategy(OperationStrategy):
    """
    The DivideStrategy class implements the division operation.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    def execute(self, a, b):
        """
        Perform division of two numbers.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of dividing a by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
