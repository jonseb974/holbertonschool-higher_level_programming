#!/usr/bin/python3
# 0-read_file.py
"""function that reads a text file (UTF8)
"""


def read_file(filename=""):
    """Read a file.
    Args:
    filename: name of the target file.
    """
    with open("filename", encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end="")
