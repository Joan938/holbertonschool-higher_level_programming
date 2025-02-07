#!/usr/bin/python3
"""Module with a class that inherits from list"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list sorted"""
        print(sorted(self))
