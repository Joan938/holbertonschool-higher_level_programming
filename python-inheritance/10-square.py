#!/usr/bin/python3
"""Module for Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initializes the square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
