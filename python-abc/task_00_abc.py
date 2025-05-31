#!/usr/bin/env python3
"""Task 00: ABC"""


from abc import ABC, abstractmethod
"""ABC module"""


class Animal(ABC):
    """Animal class"""
    @abstractmethod
    def sound(self):
        """Make a sound"""
        pass


class Dog(Animal):
    """Dog class"""
    def sound(self):
        """Make a sound"""
        return "Bark"


class Cat(Animal):
    """Cat class"""
    def sound(self):
        """Make a sound"""
        return "Meow"
