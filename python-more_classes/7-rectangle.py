#!/usr/bin/python3
# 7-rectangle.py
"""Create a rectangle."""


class Rectangle:
    """class Rectangle that defines a rectangle."""

    number_of_instances = 0
    """nb of instances."""
    print_symbol = '#'
    """print symbol"""

    def __del__(self):
        """Print message when rectangle is delete."""

        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        """Instantiation with width and height
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __repr__(self):
        """
        """
        return '{:s}({:d}, {:d})'.format(
                type(self).__name__,
                self.__width,
                self.__height
        )

    def __str__(self):
        """Draw rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        return '\n'.join(
                str(self.print_symbol) * self.__width
                for _ in range(self.__height)
        )

    @property
    def height(self):
        """Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Area
        """
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2
