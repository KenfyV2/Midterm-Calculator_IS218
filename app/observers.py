"""
This module defines observer classes for logging and auto-saving the history
of arithmetic operations performed by the Calculator class.
"""

from app.history import History

class LoggingObserver:
    """
    An observer class that logs arithmetic operations.
    """
    def update(self, operation, operand1, operand2, result):
        """
        Update the observer with the details of an arithmetic operation.

        Args:
            operation (str): The arithmetic operation performed.
            operand1 (float): The first operand.
            operand2 (float): The second operand.
            result (float): The result of the operation.
        """
        history = History(operation, operand1, operand2, result)
        print(f"Logging: {history}")

    def notify(self, message):
        """
        Notify the observer with a custom message.

        Args:
            message (str): The custom message to notify the observer with.
        """
        print(f"Notification: {message}")

class AutoSaveObserver:
    """
    An observer class that auto-saves arithmetic operations to the history.
    """
    def __init__(self, manager_history):
        """
        Initialize the AutoSaveObserver with a ManagerHistory instance.

        Args:
            manager_history (ManagerHistory): The ManagerHistory instance to save history to.
        """
        self.manager_history = manager_history

    def update(self, operation, operand1, operand2, result):
        """
        Update the observer with the details of an arithmetic operation and save it to the history.

        Args:
            operation (str): The arithmetic operation performed.
            operand1 (float): The first operand.
            operand2 (float): The second operand.
            result (float): The result of the operation.
        """
        history = History(operation, operand1, operand2, result)
        self.manager_history.add_history(history)

    def notify(self, message):
        """
        Notify the observer with a custom message.

        Args:
            message (str): The custom message to notify the observer with.
        """
        print(f"Notification: {message}")
