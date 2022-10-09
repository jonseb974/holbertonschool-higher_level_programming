#!/usr/bin/python3
# square.py
"""
class Square that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Create a class Square:
        - Class constructor:
    def __init__(self, size, x=0, y=0, id=None)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation.

        Args:
            * size (int): size of the square.
            x (int): integer.
            y (int): integer.
            id (int): id.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """ Update method

        Args:
            *args: no keyword_arguments
            **kwargs: key-worked argument like dictionary pairs k/v
        """
        my_attrs = ["size", "id", "x", "y"]

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i in range(len(args)):
                setattr(self, my_attrs[i], args[i])

    def to_dictionary(self):
        """
        Dictionary method returns
        square representation.
        """
        s = self.width
        x = self.x
        y = self.y
        i = self.id
        return {"id": i, "x": x, "size": s, "y": y}

    def __str__(self):
        """__str__ this method returns data .format style.
        """
        i = self.id
        x = self.x
        y = self.y
        size = self.width
        return "[Square] ({}) {}/{} - {}/{}.format(i, x, y size)"

    @property
    def size(self):
        """Getter method attribute size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Getter method attribut size.

        Args:
            value (int): width and height
        """
        self.width = value
        self.height = value
