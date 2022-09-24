#!/usr/bin/python3
# 4-rectangle.py
"""Rectangle creation. """


class Rectangle:
    """class Rectangle that defines a rectangle."""

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
        width of the rectangle
        """
        return(self.width)

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
    def height(self, value):
        """
        height value
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
        set value of height
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """
        perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        """
        if self.__width == 0 or self.__height == 0:
            return("")
        size = "#" * self.__width
        string = ""
        for i in range(self.__height):
            if i == (self.__height - 1):
                string += size
            else:
                string += (size + "\n")
        return(string)

    def __repr__(self):
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))
