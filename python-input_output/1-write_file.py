#!/usr/bin/python3
# 1-write_file.py
"""function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    Args:
        * filename: Name of the file.
        * text: String.
    """
    with open(filename, 'w+') as f:
        return f.write(text)
