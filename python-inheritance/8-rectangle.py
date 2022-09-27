#!/usr/bin/python3
# 8-main.py
"""class Rectangle that inherits from BaseGeometry
"""


class Rectangle:
    """class rectangle.
    """
    def __init__(self, width, height):
        """Initialisation
        Args:
            width:of rectangle.
            height: height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
