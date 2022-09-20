#!/usr/bin/python3
class Square:
    """Represent a square.
    Initialisation for a new square.
    Args:
    size (int): the size of the square.
    """

    def __init__(self, size=0):
        """Initialisation for a new square"""
        self.__size = size
        if (type(self.__size) != int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return(self.__size ** 2)
