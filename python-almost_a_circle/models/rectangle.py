#!/usr/bin/python3
# rectangle.py
"""
Write the class Rectangle
that inherits from Base.
"""
import json
from re import S
from models.base import Base


class Rectangle(Base):
    """
    This class  inherits from Base.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialisation

        Args:
            __width (int): width of the rectangle.
            __height (int): height of the rectangle.
            __x (int): x.
            __y (int): y.
            id (int): id.
        """
        # self.width = width
        # self.height = height
        # self.x = x
        # self.y = y
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Calculates area of the rectangle.
        Returns: The area of the shape.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display method.
        Prints a rectangle shape with # characters.
        """
        rectangle_shape = ""
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y

        if y > 0:
            for col in range(y):
                rectangle_shape += ("\n")
        for row in range(h):
            for i in range(x):
                rectangle_shape += (" ")
            for j in range(w):
                rectangle_shape += ("#")
            if row < h - 1:
                rectangle_shape += "\n"
        print("{}".format(rectangle_shape))

    def update(self, *args, **kwargs):
        """
        Updates method assigns to each argument an attribute.
        Args:
            - *args: a non-keyword variable argument.
            - **kwargs: pairs of key/value arguments.
            - id attributes.
            - width attributes.
            - height attributes.
            - x attributes.
            - y attributes
            """
        leag_attrs = ["id", "width", "height", "x", "y"]

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i in range(len(args)):
                setattr(self, leag_attrs[i], args[i])

    def to_dictionary(self):
        """
        This method
        returns dictionary representation of Rectangle.
        """
        w = self.__width
        h = self.__heigh
        x = self.__x
        y = self.__y
        id = self.id
        return {"id" : id, "width": w, "hight": h, "x": x, "y": y}

    def __str__(self):
        """
        This method __str__ returns .format datas.
        """
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        id = self.id
        return("[Rectangle] ({}) {}/{} - {}/{}" .format(id, x, y, w, h))

    @property
    def width(self):
        """
        Width attributes.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method width attributes.
        Args:
            -value(int): value of the width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

        @height.setter
        def height(self, value):
            """
            Set height attributes.
            define height of the rectangle.
            """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
            self.__height = value

    @property
    def height(self):
        """
        Height attributes.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Getter method for height attributes.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves x attributes.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set x attributes.
        define x.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves y attributes.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set y attributes.
        define y.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

