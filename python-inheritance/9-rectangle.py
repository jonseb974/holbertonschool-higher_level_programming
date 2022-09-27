#!/usr/bin/python3
# 9-rectangle
"""class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle.
    """
    def __init__(self, width, height):
        """ nitialisation:
            width: width of the rectangle.
            height: height of the rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return formates string.
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """method
        """
        return(self.__width * self.__height)
