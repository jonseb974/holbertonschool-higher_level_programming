#!/usr/bin/python3
"""6-load_from_json_file
Write a function that creates
an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """Function that creates
    an Object from a “JSON file”

    Args:

    filename (file): JSON file to create.
    """

    with open(filename, 'r') as f:
        return json.load(f)
