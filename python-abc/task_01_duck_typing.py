#!/usr/bin/env python3
"""Duck typing example."""

from math import pi

class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * abs(self.radius) ** 2

    def perimeter(self) -> float:
        return 2 * pi * abs(self.radius)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def shape_info(self):
    print(f"Area: {self.area()}")
    print(f"Perimeter: {self.perimeter()}")
