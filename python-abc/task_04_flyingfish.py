#!/usr/bin/env python3
"""Class FlyingFish"""


class Fish:
    """Class Fish"""
    def swim(self):
        """Method swim"""
        print("The fish is swimming.")

    def habitat(self):
        """Method habitat"""
        print("The fish lives in the water.")


class Bird:
    """Class Bird"""
    def fly(self):
        """Method fly"""
        print("The bird is flying.")

    def habitat(self):
        """Method habitat"""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """Class FlyingFish"""
    def fly(self):
        """Method fly"""
        print("The flying fish is soaring!")

    def swim(self):
        """Method swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Method habitat"""
        print("The flying fish lives both in water and the sky!")
