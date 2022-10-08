#!/usr/bin/python3
# 11-student.py
""" Write a class Student."""


class Student:
    """
    class Student represent a student.
    Public attributes:
        - first_name
        _ last_name
        _ age
    Public method to_json().
    """
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
        Return a dictionary representation
        of a Student instance.
        Args:
            attrs (list): Attributes.
        """
        if (type(attrs) = list and
                 all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of student.

        Args:
            json (dict): key/value pairs to replace
        """
        for k, v in json.items():
            setattr(self, k, v)
