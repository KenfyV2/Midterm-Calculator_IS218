"""
This module contains the REPL class for the calculator application.
"""

import logging
from app.calculator import Calculator
from app.plugins import load_plugins
from app.state_manager import StateManager

logger = logging.getLogger('app.repl')

class REPL:
    """
    The REPL class provides a command-line interface for the calculator application.
    It supports basic arithmetic operations and history management.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    def __init__(self):
        """
        Initialize the REPL with calculator and plugin commands.
        """
        self.calculator = Calculator()
        self.state_manager = StateManager('data/gpt_states.csv')
        self.plugins = load_plugins()
        self.commands = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'save_history': self.save_history,
            'load_history': self.load_history,
            'clear_history': self.clear_history,
            'delete_history': self.delete_history,
            'list_states': self.list_states,
            'get_state_details': self.get_state_details,
            'save_state_abbreviations': self.save_state_abbreviations,
            'menu': self.menu,
            'exit': self.exit
        }
        # Merge plugin commands into the REPL commands
        self.commands.update({
            name: self.create_plugin_command(func) for name, func in self.plugins.items()
        })
        logger.info("REPL initialized with commands: %s", ", ".join(self.commands.keys()))

    def run(self):
        """
        Start the REPL loop to accept and execute user commands.
        """
        logger.info("REPL started.")
        while True:
            command = input(">>> ").strip().lower()
            if command in self.commands:
                logger.debug("Executing command: %s", command)
                try:
                    self.commands[command]()
                except ValueError as e:
                    print(e)
            else:
                logger.warning("Unknown command: %s", command)
                print("Unknown command")

    def create_plugin_command(self, func):
        """
        Create a plugin command that takes two numeric inputs and returns the result.
        """
        def command():
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = func(a, b)
            print(f"Result: {result}")
            self.calculator.save_operation(func.__name__, a, b, result)
        return command

    def add(self):
        """
        Perform addition of two numbers.
        """
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = self.calculator.add(a, b)
        print(f"Result: {result}")

    def subtract(self):
        """
        Perform subtraction of two numbers.
        """
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = self.calculator.subtract(a, b)
        print(f"Result: {result}")

    def multiply(self):
        """
        Perform multiplication of two numbers.
        """
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = self.calculator.multiply(a, b)
        print(f"Result: {result}")

    def divide(self):
        """
        Perform division of two numbers.
        """
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        try:
            result = self.calculator.divide(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

    def save_history(self):
        """
        Save the calculation history to a CSV file.
        """
        filename = input("Enter filename to save history: ")
        self.calculator.save_history(filename)
        print(f"History saved to {filename}")

    def load_history(self):
        """
        Load the calculation history from a CSV file.
        """
        filename = input("Enter filename to load history: ")
        self.calculator.load_history(filename)
        print(f"History loaded from {filename}")

    def clear_history(self):
        """
        Clear the current calculation history.
        """
        self.calculator.clear_history()
        print("History cleared")

    def delete_history(self):
        """
        Delete a specified history file.
        """
        filename = input("Enter filename to delete history: ")
        self.calculator.delete_history(filename)
        print(f"History file {filename} deleted")

    def list_states(self):
        """
        List all state names.
        """
        states = self.state_manager.list_states()
        print("States:")
        for state in states:
            print(f" - {state}")

    def get_state_details(self):
        """
        Get details of a state by its abbreviation.
        """
        abbreviation = input("Enter state abbreviation: ").upper()
        details = self.state_manager.get_state_details(abbreviation)
        if details:
            print(f"Details for {abbreviation}:")
            for key, value in details.items():
                print(f" - {key}: {value}")
        else:
            print(f"No details found for state abbreviation: {abbreviation}")

    def save_state_abbreviations(self):
        """
        Save state abbreviations and names to a new CSV file.
        """
        source_csv = input("Enter source CSV filename (e.g., gpt_states.csv): ")
        target_csv = input("Enter target CSV filename (e.g., state_abbreviations.csv): ")
        self.state_manager.save_state_abbreviations(source_csv, target_csv)
        print(f"State abbreviations saved to data/{target_csv}")

    def menu(self):
        """
        Display the available commands.
        """
        print("Available commands:")
        for command in self.commands:
            print(f" - {command}")

    def exit(self):
        """
        Exit the REPL.
        """
        logger.info("Exiting REPL.")
        print("Exiting...")
        raise SystemExit
