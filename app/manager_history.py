"""
This module defines the ManagerHistory class, which manages the history of
arithmetic operations performed by the Calculator class.
"""

import os
import csv
import pandas as pd
from .history import History

class ManagerHistory:
    """
    A class to manage the history of arithmetic operations.
    """
    def __init__(self, filename='data/test_history.csv'):
        """
        Initialize the ManagerHistory with an optional filename.

        Args:
            filename (str, optional): The file to store calculator history. 
            Defaults to 'data/test_history.csv'.
        """
        self.filename = filename
        self.ensure_history_file_exists()

    def ensure_history_file_exists(self):
        """
        Ensure the history file exists. Create it if it does not exist.
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        # Create the file if it does not exist
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write('operation,operand1,operand2,result\n')  # Write header for CSV

    def load_history(self, filename=None):
        """
        Load the history from a file.

        Args:
            filename (str, optional): The filename to load the history from. Defaults to None.

        Returns:
            pd.DataFrame: The history of operations.
        """
        if filename is None:
            filename = self.filename
        history_list = []
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                try:
                    next(reader)  # Skip header
                except StopIteration:
                    # Handle empty file
                    return pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
                for row in reader:
                    if len(row) >= 4:
                        try:
                            history_list.append(History(row[0], float(row[1]),
                                                        float(row[2]), float(row[3])))
                        except ValueError:
                            # Handle rows with invalid data
                            history_list.append(History(row[0], float(row[1]),
                                                        float(row[2]), float('nan')))
                    else:
                        # Handle rows with missing data
                        history_list.append(History(row[0], float(row[1]),
                                                    float(row[2]), float('nan')))
        except FileNotFoundError:
            pass
        return pd.DataFrame([vars(h) for h in history_list])

    def save_history(self, history_list, filename=None):
        """
        Save the history to a file.

        Args:
            history_list (list or pd.DataFrame): The history to save.
            filename (str, optional): The filename to save the history to. Defaults to None.
        """
        if filename is None:
            filename = self.filename
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['operation', 'operand1', 'operand2', 'result'])  # Write header
            if isinstance(history_list, list):
                for history in history_list:
                    writer.writerow([history.operation, history.operand1,
                                     history.operand2, history.result])
            else:
                for _, row in history_list.iterrows():
                    writer.writerow([row['operation'], row['operand1'],
                                     row['operand2'], row['result']])

    def clear_history(self):
        """
        Clear the history file.
        """
        with open(self.filename, 'w', encoding='utf-8'):
            pass

    def add_history(self, history):
        """
        Add a history record.

        Args:
            history (History): The history record to add.
        """
        history_list = self.load_history()
        new_record = pd.DataFrame([vars(history)])
        history_list = pd.concat([history_list, new_record], ignore_index=True)
        self.save_history(history_list)

    def print_history(self):
        """
        Print the history to the console.
        """
        history_list = self.load_history()
        for _, row in history_list.iterrows():
            print(f"{row['operation']},{row['operand1']},{row['operand2']},{row['result']}")

    def save_to(self, filename):
        """
        Save the history to a specified file.

        Args:
            filename (str): The filename to save the history to.
        """
        history_list = self.load_history()
        self.save_history(history_list, filename)

    def load_from(self, filename):
        """
        Load the history from a specified file.

        Args:
            filename (str): The filename to load the history from.
        """
        history_list = self.load_history(filename)
        self.save_history(history_list)
