#!/usr/bin/python3
# 9-rectangle.py
"""rectangle."""


class Rectangle:
    """class Rectangle that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialisation of rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Self
        """
        string = ((str(self.print_symbol) * self.__width) + '\n')*self.__height
        return(string[: -1])

    def __dell__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Width
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """Width
        """
        if not isinstance(value, int):
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
        """ Height set"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area
        """
        return(self.__height * self.__width)

    def perimeter(self):
        """Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return(0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or (rect_1.area() > rect_2.area()):
            return(rect_1)
        return(rect_2)

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
