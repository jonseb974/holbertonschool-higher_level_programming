#!/usr/bin/python3
# rectangle.py
"""Write the class Rectangle that inherits from Base.
"""
import json
from re import S
from models.base import Base


class Rectangle(Base):
    """This class  inherits from Base.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation

        Args:
            __width (int): width of the rectangle.
            __height (int): height of the rectangle.
            __x (int): x.
            __y (int): y.
            id: id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """
            Width attributes.
            """
            return self.__width

        @property
        def height(self):
            """Height attributes.
            """
            return self.__height

        @property
        def x(self):
            """Retrieves x attributes.
            """
            return self.__x

        @property
        def y(self):
            """Retrieves y attributes.
            """
            return self.__y

        @width.setter
        def width(self, value):
            """Set width attributes.
            """

            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """Set height attributes.
            """

            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @x.setter
        def x(self, value):
            """Set x attributes.
            """
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @y.setter
        def y(self, value):
            """Set y attributes.
            """

            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """Calculates area of the rectangle.

            Returns: area
            """
            return self.__width * self.__height

        def display(self):
            """Prints a rectangle shape with # character.
            """
            for y in range(0, self.__y):
                print()
            for i in range(0, self.__height):
                for x in range(0, self.__x):
                    print(" ", end="")
                for j in range(0, self.__width):
                    print("#", end="")
                print()

        def __str__(self):
            """Returns a string for the Rectangle shape.
            """
            s = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height)
            return s

        def update(self, *args, **kwargs):
            """Updates attributes.
            Args:
                - id attributes.
                - width attributes
                - height attributes
                - x attributes
                - y attributes
            """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        def to_dictionary(self):
            """Returns
            dictioanary of Rectangle.
            """
            my_dict = {"id": self.id,
                       "width": self.__width,
                       "hight": self.__height,
                       "x": self.__x,
                       "y": self.__y
                       }
            return my_dict
