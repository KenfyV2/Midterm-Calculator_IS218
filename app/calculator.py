"""
This module defines the Calculator class, which provides basic arithmetic operations
and manages the history of these operations.
"""

import logging
import pandas as pd
from app.calculator_config import CalculatorConfig
from app.strategy_factory import StrategyFactory

logger = logging.getLogger('app.calculator')

class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations and manage history.
    """
    def __init__(self, config=None):
        """
        Initialize the Calculator with an optional configuration.

        Args:
            config (CalculatorConfig, optional): Configuration for the calculator. Defaults to None.
        """
        self.config = config if config else CalculatorConfig()
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
        self.observers = []
        logger.info("Calculator initialized with empty history.")

    def add_observer(self, observer):
        """
        Add an observer to the calculator.

        Args:
            observer: The observer to add.
        """
        self.observers.append(observer)

    def notify_observers(self, operation, a, b, result):
        """
        Notify all observers of an operation.

        Args:
            operation (str): The operation performed.
            a (float): The first operand.
            b (float): The second operand.
            result (float): The result of the operation.
        """
        for observer in self.observers:
            observer.update(operation, a, b, result)

    def save_operation(self, operation, a, b, result):
        """
        Save an operation to the history.

        Args:
            operation (str): The operation performed.
            a (float): The first operand.
            b (float): The second operand.
            result (float): The result of the operation.
        """
        new_record = pd.DataFrame([{
            'operation': operation,
            'operand1': a,
            'operand2': b,
            'result': result
        }])
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.notify_observers(operation, a, b, result)

    def load_history(self, filename=None):
        """
        Load the history from a file.

        Args:
            filename (str, optional): The filename to load the history from. Defaults to None.
        """
        filename = filename or self.config.calculator_history_file
        try:
            self.history = pd.read_csv(filename)
            logger.info("Calculator history loaded from file: %s", filename)
        except FileNotFoundError:
            logger.warning("History file not found: %s", filename)
        except pd.errors.EmptyDataError:
            logger.warning("History file is empty: %s", filename)

    def execute_operation(self, operation, a, b):
        """
        Execute an operation using the specified strategy.

        Args:
            operation (str): The operation to perform.
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the operation.
        """
        strategy = StrategyFactory.create_strategy(operation)
        result = strategy.execute(a, b)
        self.save_operation(operation, a, b, result)
        return result

    def get_history(self):
        """
        Get the history of operations.

        Returns:
            pd.DataFrame: The history of operations.
        """
        return self.history
