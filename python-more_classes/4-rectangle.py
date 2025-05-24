#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """This class defines a simple Rectangle."""

    def __init__(self, width=0, height=0):
        """Create a new Rectangle with the given width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of this Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of this Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of this Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of this Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of this Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of this Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a printable string representation of this Rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for i in range(self.height)])

    def __repr__(self):
        """Return a string representation of this Rectangle that can be used to
        create a new instance of this class."""
        return "Rectangle({}, {})".format(self.width, self.height)
