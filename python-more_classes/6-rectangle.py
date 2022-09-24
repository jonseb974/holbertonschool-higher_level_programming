#!/usr/bin/python3
# 6-rectangle.py
"""create a rectangle. """


class Rectangle:
    """class Rectangle that defines a rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Instantiation with width and height.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Area
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Self
        """
        if self.__width == 0 or self.__height == 0:
            return("")
        size = "#" * self.__width
        string = ("")
        for i in range(self.__height):
            if i == self.__height - 1:
                string += size
            else:
                sting += (size + "\n")
        return(string)

    def __repr__(self):
        """Print width and height
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
