#!/usr/bin/python3
# 4-print_square.py
"""
print a square shape
using '#' characters
"""


def print_square(size):
    """ print a square
    Args:
    size (int): length and width
    of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size) < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        print('#', end='')
