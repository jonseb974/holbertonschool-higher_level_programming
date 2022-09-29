#!/usr/bin/python3
# 2-append_write.py
"""function that appends a string
at the end of a text file that writes
a string to a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file.
        Args:
            filename: Name of the file.
            text: String.
    """
    with open(filename, 'a+') as f:
        return f.write(text)
