#!/usr/bin/python3
"""
This module provides a function to print a square using the character `#`.

The function `print_square` takes an integer `size` and prints a square of
that size using the `#` character.

Requirements:
- `size` must be an integer.
- If `size` is less than 0, a ValueError is raised.
- If `size` is a float, a TypeError is raised.

Raises:
- TypeError: If `size` is not an integer.
- ValueError: If `size` is less than 0.

Example usage:
>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    Prints a square with the character `#`.

    Parameters:
    size (int): The size length of the square sides.

    Returns:
    None

    Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
