#!/usr/bin/python3
"""Represent a square."""


class Square:
    """ class square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialised a new square
        Args:
        size (int): size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set current position of square.
        """
        return(self.__position)

    @position.setter
    def position(self, value):
        """Set position.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area.
        """
        return(self.__size ** 2)

    def my_print(self):
        """Print square with '#' character,
        at position given by position attribute.
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
                for row in range(0, self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)
