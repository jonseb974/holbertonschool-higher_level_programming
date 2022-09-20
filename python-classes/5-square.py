#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialisation of the size."""
        self.size = size

    @property
    def size(self):
        """set current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """define value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns current area of square"""
        return(self.__size ** 2)

    def my_print(self):
        """print a square shape using "#" characters."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
