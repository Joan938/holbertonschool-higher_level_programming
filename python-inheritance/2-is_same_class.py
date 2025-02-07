#!/usr/bin/python3
"""Module for is_same_class method."""


def is_same_class(obj, a_class):
    """Method to check if an object is an instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
