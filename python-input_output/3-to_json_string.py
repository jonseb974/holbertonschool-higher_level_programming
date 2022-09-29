#!/usr/bin/python3
# 3-to_json_string.py
"""Write a function that returns
the JSON representation of an object (string)
"""


import json

"""function that returns the JSON
representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """function that returns the JSON
    Args:
        my_obj: string
    """
    return json.dumps(my_obj)
