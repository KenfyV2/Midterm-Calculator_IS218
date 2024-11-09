"""
This module defines the REPL class, which provides a command-line interface
for the Calculator application.
"""

import logging
import os
import importlib.util
import pandas as pd
from app.calculator import Calculator
from app.observers import LoggingObserver, AutoSaveObserver
from app.manager_history import ManagerHistory

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
        self.history_manager = ManagerHistory()
        self.logging_observer = LoggingObserver()
        self.auto_save_observer = AutoSaveObserver(self.history_manager)
        self.calculator.add_observer(self.logging_observer)
        self.calculator.add_observer(self.auto_save_observer)
        self.commands = {
            'history': self.show_history,
            'clear': self.clear_history,
            'save': self.save_history,
            'save_to': self.save_to,
            'load': self.load_history,
            'load_from': self.load_from,
            'menu': self.menu,
            'exit': self.exit
        }
        self.load_plugins()
        logger.info("REPL initialized with commands: %s", ", ".join(self.commands.keys()))

        # Load calculator history from file
        self.calculator.load_history()

    def load_plugins(self):
        """
        Load plugins from the plugins directory and register their commands.
        """
        plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py'):
                plugin_name = filename[:-3]
                plugin_path = os.path.join(plugins_dir, filename)
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, plugin_name):
                    self.commands[plugin_name] = self.create_plugin_command(getattr(module,
                                                                                    plugin_name))

    def create_plugin_command(self, func):
        """
        Create a plugin command that takes two numeric inputs and returns the result.
        """
        def command():
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = func(a, b)
                print(f"Result: {result}")
                self.calculator.save_operation(func.__name__, a, b, result)
            except ValueError as e:
                print(f"Error: {e}")
        return command

    def show_history(self):
        """
        Show the history of operations.
        """
        self.history_manager.print_history()

    def clear_history(self):
        """
        Clear the history of operations.
        """
        self.history_manager.clear_history()
        self.calculator.history = pd.DataFrame(columns=['operation', 'operand1',
                                                        'operand2', 'result'])

    def save_history(self):
        """
        Save the current history to the default file.
        """
        current_history = self.calculator.get_history()
        self.history_manager.save_history(current_history)

    def save_to(self):
        """
        Save the current history to a specified file.
        """
        filename = input("Enter filename to save history in data folder (example.csv): ")
        filepath = os.path.join('data', filename)
        self.history_manager.save_to(filepath)
        print(f"History saved to {filepath}")

    def load_history(self):
        """
        Load history from a specified file.
        """
        filename = input("Enter filename to load history from data folder: ")
        data_folder = 'data'
        source_path = os.path.join(data_folder, filename)
        self.history_manager.load_from(source_path)
        self.calculator.history = self.history_manager.load_history()
        print(f"History loaded from {source_path}")

    def load_from(self):
        """
        Load history from a specified file.
        """
        filename = input("Enter filename to load history from data folder: ")
        filepath = os.path.join('data', filename)
        self.history_manager.load_from(filepath)
        self.calculator.history = self.history_manager.load_history()
        print(f"History loaded from {filepath}")

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

    def run(self):
        """
        Run the REPL loop, accepting and executing commands.
        """
        while True:
            command = input("Enter command: ").strip().lower()
            if command in self.commands:
                self.commands[command]()
            else:
                print("Unknown command")

if __name__ == "__main__":
    repl = REPL()
    repl.run()
