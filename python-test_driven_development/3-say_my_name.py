#!/usr/bin/python3
# 3-say_my_name.py
"""
print My name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints
    My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
