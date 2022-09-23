#!/usr/bin/python3
"""
Represent a square
"""


class Square:
    """
    Square classRepresente a square.
    Private instance attribute: size:
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
    Private instance attribute: position:
    - property def position(self): to retrieve it
    - property setter def position(self, value)
    Instantiation with optional size and optional position
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialised a new square
        Args:
        size (int): size of the square
        """
        self.size = size
        sefl.position = position

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set current position of square"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """Set position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns current square area."""
        return(sel.__size ** 2)

    def my_print(self):
        """Print square with '#' character,
        at position given by position attribute.
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0 self.__size):
                print('#', end="")
            print()
