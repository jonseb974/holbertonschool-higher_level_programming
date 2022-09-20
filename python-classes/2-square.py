#!/usr/bin/python3
# 2-square
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(size, size=0):
        """Initialisation to create the square.

        Args:
            size: The size of the new_square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
