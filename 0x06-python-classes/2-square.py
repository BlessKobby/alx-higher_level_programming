#!/usr/bin/python3
# 2-square.py
"""Definition of the class square."""


class Square:
    """Body of the square class"""

    def __init__(self, size=0):
        """Square class contructor.
        Args:
            size (int): The size of the New Square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer value.")
        elif size < 0:
            raise ValueError("Size must be >= 0.")
        self.__size = size
