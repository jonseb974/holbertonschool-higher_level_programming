#!/usr/bin/python3
"""Define square"""


class Square:
    """define square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialised a new square
        Args:
        size (int): size of the square
        """
        self.__size = size
        sefl.position = position

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set current position of square"""
        return(self.__position)

    @position.setter
