"""
This module defines the root function, which performs root calculation of a number.
"""

def root(a, b):
    """
    Perform root calculation of a number.

    Args:
        a (float): The number to take the root of.
        b (float): The root to take.

    Returns:
        float: The result of taking the `b`-th root of `a`.

    Raises:
        ValueError: If the root `b` is zero.
    """
    if b == 0:
        raise ValueError("Cannot take root with zero")
    return a ** (1 / b)
