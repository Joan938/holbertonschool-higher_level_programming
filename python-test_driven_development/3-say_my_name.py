#!/usr/bin/python3
"""
This module provides a function to print a person's full name.

The function `say_my_name` takes a first name and an optional last name,
validates them as strings, and prints the full name in the format:

    "My name is <first name> <last name>"

Raises:
- TypeError: If first_name or last_name is not a string.

Example usage:
>>> say_my_name("John", "Doe")
My name is John Doe

>>> say_my_name("Alice")
My name is Alice
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Parameters:
    first_name (str): The first name (required).
    last_name (str): The last name (optional, defaults to an empty string).

    Returns:
    None

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
