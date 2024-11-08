"""
This module provides strategy classes for different arithmetic operations.
"""

class OperationStrategy:
    """
    The OperationStrategy class defines the interface for arithmetic operations.
    """
    def execute(self, a, b):
        raise NotImplementedError("You should implement this method.")

class AddStrategy(OperationStrategy):
    """
    The AddStrategy class implements the addition operation.
    """
    def execute(self, a, b):
        return a + b

class SubtractStrategy(OperationStrategy):
    """
    The SubtractStrategy class implements the subtraction operation.
    """
    def execute(self, a, b):
        return a - b

class MultiplyStrategy(OperationStrategy):
    """
    The MultiplyStrategy class implements the multiplication operation.
    """
    def execute(self, a, b):
        return a * b

class DivideStrategy(OperationStrategy):
    """
    The DivideStrategy class implements the division operation.
    """
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
