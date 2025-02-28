#!/usr/bin/env python3
"""Create a custom class"""

import pickle
import os


class CustomObject:
    """Custom class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")
        if os.path.getsize(filename) == 0:
            raise EOFError("File is empty.")
        with open(filename, 'rb') as f:
            return pickle.load(f)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)
