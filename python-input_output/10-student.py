#!/usr/bin/python3
"""10-student.py
Write a class Student that defines
a student by:(based on 9-student.py)
"""


class Student:
    """A class Student.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method

        Args:
            attrs (_type_, optional): _description_. Defaults to None.
        """
        if (type(attrs) == list and
           all(type(elem) == str for elem in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
