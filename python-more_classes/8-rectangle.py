#!/usr/bin/python3
"""Module to define a rectangle"""


class Rectangle:
    """Class for the rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instance of a rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property to retrieve the width of the rectangle

        Returns:
            width: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set the value of the width

        Args:
            value (int): The value of the width to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve the height of the rectangle

        Returns:
            height: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set the value of the height

        Args:
            value (int): The value of the height to set
        """
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
        """Method that returns the string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (
            "\n".join([
                str(self.print_symbol) * self.__width
                for i in range(self.__height)
            ])
        )

    def __repr__(self):
        """Method that returns the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method that deletes an instance of Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle

        Returns:
            rect_1: The first rectangle if both have the same area
            rect_2: The second rectangle if rect_2 is bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
