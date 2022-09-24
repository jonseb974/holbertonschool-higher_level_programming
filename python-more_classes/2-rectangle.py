#!/usr/bin/python3
# 2-rectangle.py
"""Define a rectangle."""


class Rectangle:
    """
    class Rectangle that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialisation datas.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width of the rectangle.
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """
        Width
        TypeError message
        """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height of the rectangle
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
        height
        TypeError message
        """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        Rectangle area
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """
        Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)
