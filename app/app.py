"""
This module contains the App class which initializes and runs the REPL.
"""

from .repl import REPL

class App:
    """
    The App class initializes and runs the REPL.
    """
    # Disable the "too few public methods" warning for this class
    # pylint: disable=too-few-public-methods
    def __init__(self):
        """
        Initialize the App with a REPL instance.
        """
        self.repl = REPL()

    def run(self):
        """
        Run the REPL.
        """
        self.repl.run()
