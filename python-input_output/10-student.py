#!/usr/bin/python3
""" 10-student.py"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes student class"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Returns dictionary representation of student"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key in attrs:
            if hasattr(self, key):
                new_dict[key] = getattr(self, key)
        return new_dict
