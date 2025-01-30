#!/usr/bin/python3
"""
This module defines a Square class that represents a square.

Classes:
    Square: A class that defines a square by its size and provides methods to
            calculate its area and print the square using the '#' character.

Methods:
    __init__(self, size=0): Initializes a new Square instance.
    size(self): Retrieves the size of the square.
    size(self, value): Sets the size of the square with validation.
    area(self): Returns the current square area.
    my_print(self): Prints the square with the character '#'.
"""


class Square:
    """ A class to represent a square. """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
