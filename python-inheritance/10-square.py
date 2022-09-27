#!/usr/bin/python3
# 10-square.py
"""class Square
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square
    Private instance attribute size.
    Public method area()
    """
    def __init__(self, size):
        """Instantiation
        Args:
            size (int): size of the rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method area
        """
        return(self.__size ** 2)
