#!/usr/bin/python3
"""Square class definition."""


class Square:
    """Square class body."""

    def __init__(self, size=0):
        """Square contructor.
        Args:
            size (int): The size of the New Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer value.")
        elif size < 0:
            raise ValueError("Size must be >= 0.")
        self.__size = size

    def area(self):
        """Returns the new area of the square."""
        return (self.__size * self.__size)
