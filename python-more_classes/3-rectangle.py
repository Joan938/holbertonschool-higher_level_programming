#!/usr/bin/python3
"""Module that defines a class Rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes an object for a rectangle class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method that returns a string that represents the object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]
