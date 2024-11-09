"""
This module contains unit tests for the ManagerHistory class.
"""

import os
import pandas as pd  # Import pandas
from app.manager_history import ManagerHistory
from app.history import History

def test_ensure_history_file_exists():
    """
    Test that the history file is created if it does not exist.
    """
    manager = ManagerHistory('data/test_history.csv')
    manager.ensure_history_file_exists()
    assert os.path.exists('data/test_history.csv')

def test_load_history():
    """
    Test loading history from a file.
    """
    manager = ManagerHistory('data/test_history.csv')
    manager.clear_history()  # Clear history before loading
    history = manager.load_history()
    assert isinstance(history, pd.DataFrame)
    assert history.empty

def test_save_history():
    """
    Test saving history to a file.
    """
    manager = ManagerHistory('data/test_history.csv')
    history = [History('add', 1, 2, 3)]
    manager.save_history(history)
    loaded_history = manager.load_history()
    assert len(loaded_history) == 1

def test_clear_history():
    """
    Test clearing the history file.
    """
    manager = ManagerHistory('data/test_history.csv')
    manager.clear_history()
    history = manager.load_history()
    assert history.empty

def test_add_history():
    """
    Test adding a history record.
    """
    manager = ManagerHistory('data/test_history.csv')
    history = History('add', 1, 2, 3)
    manager.add_history(history)
    loaded_history = manager.load_history()
    assert len(loaded_history) == 1

def test_print_history(capsys):
    """
    Test printing the history to the console.
    """
    manager = ManagerHistory('data/test_history.csv')
    history = History('add', 1, 2, 3)
    manager.add_history(history)
    manager.print_history()
    captured = capsys.readouterr()
    assert "add,1.0,2.0,3.0" in captured.out

def test_save_to(tmp_path):
    """
    Test saving history to a specified file.
    """
    manager = ManagerHistory('data/test_history.csv')
    history = [History('add', 1, 2, 3)]
    manager.save_history(history)
    save_path = tmp_path / "saved_history.csv"
    manager.save_to(str(save_path))
    assert os.path.exists(save_path)
    loaded_history = pd.read_csv(save_path)
    assert len(loaded_history) == 1
    assert loaded_history.iloc[0]['operation'] == 'add'
    assert loaded_history.iloc[0]['operand1'] == 1
    assert loaded_history.iloc[0]['operand2'] == 2
    assert loaded_history.iloc[0]['result'] == 3

def test_load_from(tmp_path):
    """
    Test loading history from a specified file.
    """
    manager = ManagerHistory('data/test_history.csv')
    save_path = tmp_path / "saved_history.csv"
    history = pd.DataFrame([{
        'operation': 'add',
        'operand1': 1,
        'operand2': 2,
        'result': 3
    }])
    history.to_csv(save_path, index=False)
    manager.load_from(str(save_path))
    loaded_history = manager.load_history()
    assert len(loaded_history) == 1
    assert loaded_history.iloc[0]['operation'] == 'add'
    assert loaded_history.iloc[0]['operand1'] == 1
    assert loaded_history.iloc[0]['operand2'] == 2
    assert loaded_history.iloc[0]['result'] == 3

def test_load_history_file_not_found():
    """
    Test loading history from a non-existent file.
    """
    manager = ManagerHistory('data/non_existent_file.csv')
    history = manager.load_history()
    assert isinstance(history, pd.DataFrame)
    assert history.empty

def test_load_history_empty_file(tmp_path):
    """
    Test loading history from an empty file.
    """
    empty_file = tmp_path / "empty_history.csv"
    empty_file.touch()  # Create an empty file
    manager = ManagerHistory(str(empty_file))
    history = manager.load_history()
    assert isinstance(history, pd.DataFrame)
    assert history.empty

def test_load_history_with_invalid_data(tmp_path):
    """
    Test loading history from a file with invalid data.
    """
    invalid_file = tmp_path / "invalid_history.csv"
    with open(invalid_file, 'w', encoding='utf-8') as f:
        f.write("invalid,data\n")
    manager = ManagerHistory(str(invalid_file))
    history = manager.load_history()
    assert isinstance(history, pd.DataFrame)
    assert history.empty

def test_load_history_with_partial_data(tmp_path):
    """
    Test loading history from a file with partial data.
    """
    partial_file = tmp_path / "partial_history.csv"
    with open(partial_file, 'w', encoding='utf-8') as f:
        f.write("operation,operand1,operand2,result\nadd,1,2\n")
    manager = ManagerHistory(str(partial_file))
    history = manager.load_history()
    assert isinstance(history, pd.DataFrame)
    assert len(history) == 1
    assert history.iloc[0]['operation'] == 'add'
    assert history.iloc[0]['operand1'] == 1
    assert history.iloc[0]['operand2'] == 2
    assert pd.isna(history.iloc[0]['result'])

def test_load_history_with_malformed_data(tmp_path):
    """
    Test loading history from a file with malformed data.
    """
    malformed_file = tmp_path / "malformed_history.csv"
    with open(malformed_file, 'w', encoding='utf-8') as f:
        f.write("operation,operand1,operand2,result\nadd,1,2,three\n")
    manager = ManagerHistory(str(malformed_file))
    history = manager.load_history()
    assert isinstance(history, pd.DataFrame)
    assert len(history) == 1
    assert history.iloc[0]['operation'] == 'add'
    assert history.iloc[0]['operand1'] == 1
    assert history.iloc[0]['operand2'] == 2
    assert pd.isna(history.iloc[0]['result'])

def test_load_history_with_extra_columns(tmp_path):
    """
    Test loading history from a file with extra columns.
    """
    extra_columns_file = tmp_path / "extra_columns_history.csv"
    with open(extra_columns_file, 'w', encoding='utf-8') as f:
        f.write("operation,operand1,operand2,result,extra\nadd,1,2,3,extra_data\n")
    manager = ManagerHistory(str(extra_columns_file))
    history = manager.load_history()
    assert isinstance(history, pd.DataFrame)
    assert len(history) == 1
    assert history.iloc[0]['operation'] == 'add'
    assert history.iloc[0]['operand1'] == 1
    assert history.iloc[0]['operand2'] == 2
    assert history.iloc[0]['result'] == 3
