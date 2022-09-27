#!/usr/bin/python3
# 2-is_same_class.py
"""function that check instance
"""


def is_same_class(obj, a_class):
    """class object
    Args:
    obj: object to check.
    a_class: class to compare to.
    Return True or Fale.
    """
    return True if type(obj) is a_class else False
