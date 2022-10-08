#!/usr/bin/python3
# base.py
""" Write the first class Base."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Attributes:
        __nb_objects (int):Nb of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation.

        Args:
            id (int): Identtity of the base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
