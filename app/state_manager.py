"""
This module provides functionality to manage state data from a CSV file.
"""

import pandas as pd
import os

class StateManager:
    """
    The StateManager class provides methods to manage state data.
    """
    def __init__(self, csv_file):
        self.states = pd.read_csv(csv_file)

    def list_states(self):
        """
        List all state names.
        """
        return self.states['State Name'].tolist()

    def get_state_details(self, state_abbreviation):
        """
        Get details of a state by its abbreviation.
        """
        state = self.states[self.states['State Abbreviation'] == state_abbreviation]
        if not state.empty:
            return state.to_dict(orient='records')[0]
        else:
            return None

    def save_state_abbreviations(self, source_csv, target_csv):
        """
        Save state abbreviations and names to a new CSV file.
        """
        source_csv = os.path.join('data', source_csv)
        target_csv = os.path.join('data', target_csv)
        states = pd.read_csv(source_csv)
        state_abbreviations = states[['State Abbreviation', 'State Name']]
        os.makedirs(os.path.dirname(target_csv), exist_ok=True)
        state_abbreviations.to_csv(target_csv, index=False)