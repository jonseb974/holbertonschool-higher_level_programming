#!/usr/bin/python3
class Square:
    """Represent a square.
    Initialisation for a new square.
    Args:
    size (int): the size of the square.
    """

    def __init__(self, size=0):
        """Initialisation for a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return(self.__size ** 2)
