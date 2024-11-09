"""
This module defines the StrategyFactory class, which provides a factory method
for creating instances of different arithmetic operation strategies.
"""

from app.strategies import (
    AddStrategy, SubtractStrategy, MultiplyStrategy,
    DivideStrategy, PowerStrategy, RootStrategy
)

class StrategyFactory:
    """
    A factory class for creating instances of different arithmetic operation strategies.
    """
    @staticmethod
    def create_strategy(operation):
        """
        Create an instance of the strategy for the given operation.

        Args:
            operation (str): The operation for which to create a strategy.

        Returns:
            OperationStrategy: An instance of the strategy for the given operation.

        Raises:
            ValueError: If the operation is not supported.
        """
        if operation == 'add':
            return AddStrategy()
        if operation == 'subtract':
            return SubtractStrategy()
        if operation == 'multiply':
            return MultiplyStrategy()
        if operation == 'divide':
            return DivideStrategy()
        if operation == 'power':
            return PowerStrategy()
        if operation == 'root':
            return RootStrategy()
        raise ValueError(f"Operation '{operation}' is not supported")

    @staticmethod
    def supported_operations():
        """
        Get a list of supported operations.

        Returns:
            list: A list of supported operations.
        """
        return ['add', 'subtract', 'multiply', 'divide', 'power', 'root']
