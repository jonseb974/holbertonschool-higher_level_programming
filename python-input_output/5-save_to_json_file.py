#!/usr/bin/python3
# 5-save_to_json_file.py
"""Write a function that writes an Object
to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes
    an Object to a text file,
    using a JSON representation

    Args:
        my_obj (objet): Object
        filename (file): File
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
