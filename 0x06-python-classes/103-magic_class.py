#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math


class MagicClass:
    """Initialization of the Magic-Class."""
    def __init__(self, radius=0):
        """magic class constructor"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a numeral.")
        self._MagicClass__radius = radius

    def area(self):
        """Calculates the area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference."""
        return 2 * math.pi * self._MagicClass__radius
