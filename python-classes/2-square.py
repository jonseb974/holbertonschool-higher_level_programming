#!/usr/bin/python3
"""class Square to define a square."""


class Square:
    """Class square."""
    def __init__(self, size=0):
        """
        Method __init__: Initialisation to create the square.
        __size: attribute
        size: the size of the new_square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
