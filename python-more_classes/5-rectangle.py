#!/usr/bin/python3
""" Module that defines a class Rectangle """


class Rectangle:
    """ Class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Method that initializes the instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method that sets the value of the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method that sets the value of the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Method that returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Method that returns the string representation of the instance """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """ Method that returns the string representation of the instance """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Method that deletes the instance """
        print("Bye rectangle...")
