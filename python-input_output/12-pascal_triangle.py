#!/usr/bin/python3
# 12-pascal_triangle.py
"""Defines a class Student. """


class Student:
    """Represent a class student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialisation.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get dictionary representation of a student
        Args:
            attrs (list): Some attributes.
        """
        if(type(attrs) == list and
           all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
