# Midterm-Calculator_IS218
# Advanced Python Calculator

## Project Overview

This project is an advanced Python-based calculator application designed for a software engineering graduate course. The application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone git@github.com:KenfyV2/Midterm-Calculator_IS218.git
    cd Midterm-Calculator_IS218
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    ENVIRONMENT=development
    DEBUG=True
    ```

## Usage Examples

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Use the REPL**:
    ```sh
    >>> menu
    Available commands:
    - add
    - subtract
    - multiply
    - divide
    - power
    - root
    - history
    - clear
    - save
    - load
    - menu
    - exit
    >>> exit
    Exiting...
    ```

## Design Patterns

### Facade Pattern
The `Calculator` class acts as a facade.

### Factory Method Pattern
Used in the `StrategyFactory` class to create instances of different arithmetic operation strategies.

### Strategy Pattern
Used in the `Calculator` class to perform different arithmetic operations.

## Environment Variables

Environment variables are used to configure the application dynamically. The `.env` file contains the following variables:
- `ENVIRONMENT`: The environment in which the application is running (e.g., development, production).
- `DEBUG`: A flag to enable or disable debug mode.

**Code Example**:
```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
environment = os.getenv('ENVIRONMENT')
debug = os.getenv('DEBUG')

print(f"Environment: {environment}")
print(f"Debug: {debug}")
```

## Logging

Logging is implemented using the `logging` module. The logging configuration is defined in `logging.conf`. Logs are written to both the console and a file (`app.log`).

**Code Example**:
```python
import logging
import logging.config

# Load logging configuration
logging.config.fileConfig('logging.conf')

# Create a logger
logger = logging.getLogger('app')

logger.info('This is an info message')
logger.error('This is an error message')
```

## Exception Handling

Exception handling is implemented using try/except blocks to manage errors gracefully. The application uses both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches.

**Code Example (LBYL)**:
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```
**Code Example (EAFP)**:
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
```

## Testing

Run tests using `pytest`:
```sh
pytest
```

Check code quality using `pylint`:
```sh
pylint app tests
```

## GitHub Actions
The CI/CD pipeline is set up using GitHub Actions. The workflow file is located at .github/workflows/python-app.yml. It runs tests and checks code quality on every push and pull request to the main branch.

## Video Demonstration
[Link to video demonstration](https://drive.google.com/file/d/1ojcp6sMcG1T9oc2wKbLPQOIeuLdPK22Q/view?usp=sharing)

## License
This project is licensed under the MIT License. See the LICENSE file for details.
