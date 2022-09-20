#!/usr/bin/python3
# 2-square.py
"""Define class square."""


class Square:
    """Class square."""

    def __init__(self, size=0):
        """Initialisation to create the square.
        Args:
        size (int): size of the square.
        __size: attribute

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
