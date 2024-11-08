"""
This module contains the Calculator class which performs arithmetic operations
and manages the calculation history.
"""

import pandas as pd
import os
import logging

logger = logging.getLogger('app.calculator')

class Calculator:
    """
    The Calculator class performs arithmetic operations and manages the calculation history.
    """
    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
        logger.info("Calculator initialized with empty history.")

    def add(self, a, b):
        """
        Perform addition of two numbers and save the result to history.
        """
        result = a + b
        self._save_history('add', a, b, result)
        logger.debug("Performed addition: %s + %s = %s", a, b, result)
        return result

    def subtract(self, a, b):
        """
        Perform subtraction of two numbers and save the result to history.
        """
        result = a - b
        self._save_history('subtract', a, b, result)
        logger.debug("Performed subtraction: %s - %s = %s", a, b, result)
        return result

    def multiply(self, a, b):
        """
        Perform multiplication of two numbers and save the result to history.
        """
        result = a * b
        self._save_history('multiply', a, b, result)
        logger.debug("Performed multiplication: %s * %s = %s", a, b, result)
        return result

    def divide(self, a, b):
        """
        Perform division of two numbers and save the result to history.
        Raise a ValueError if division by zero is attempted.
        """
        if b == 0:
            logger.error("Attempted to divide by zero.")
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._save_history('divide', a, b, result)
        logger.debug("Performed division: %s / %s = %s", a, b, result)
        return result

    def _save_history(self, operation, operand1, operand2, result):
        """
        Save the operation and its result to the calculation history.
        """
        new_record = pd.DataFrame([{
            'operation': operation,
            'operand1': operand1,
            'operand2': operand2,
            'result': result
        }])
        # Ensure the new record DataFrame has the same columns as the history DataFrame
        new_record = new_record.reindex(columns=self.history.columns)
        # Exclude empty or all-NA entries before concatenation
        if not new_record.isna().all().all():
            self.history = pd.concat([self.history, new_record], ignore_index=True)
            logger.info("Saved history: %s", new_record.to_dict(orient='records'))

    def save_history(self, filename):
        """
        Save the calculation history to a CSV file.
        """
        self.history.to_csv(filename, index=False)
        logger.info("History saved to %s", filename)

    def load_history(self, filename):
        """
        Load the calculation history from a CSV file.
        """
        if os.path.exists(filename):
            self.history = pd.read_csv(filename)
            logger.info("History loaded from %s", filename)
        else:
            logger.warning("History file %s does not exist", filename)

    def clear_history(self):
        """
        Clear the current calculation history.
        """
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
        logger.info("History cleared")

    def delete_history(self, filename):
        """
        Delete a specified history file.
        """
        if os.path.exists(filename):
            os.remove(filename)
            logger.info("History file %s deleted", filename)
        else:
            logger.warning("History file %s does not exist", filename)