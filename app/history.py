"""
This module defines the History class, which represents an arithmetic operation
and its operands and result.
"""

class History:
    """
    A class to represent an arithmetic operation and its operands and result.
    """
    def __init__(self, operation, operand1, operand2, result):
        """
        Initialize the History object with the operation, operands, and result.

        Args:
            operation (str): The arithmetic operation performed.
            operand1 (float): The first operand.
            operand2 (float): The second operand.
            result (float): The result of the operation.
        """
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result

    def __str__(self):
        """
        Return a string representation of the History object.

        Returns:
            str: A string representation of the History object.
        """
        return f"{self.operation},{self.operand1},{self.operand2},{self.result}"

    def to_dict(self):
        """
        Return a dictionary representation of the History object.

        Returns:
            dict: A dictionary representation of the History object.
        """
        return {
            'operation': self.operation,
            'operand1': self.operand1,
            'operand2': self.operand2,
            'result': self.result
        }
