#!/usr/bin/python3
"""7-add_item.py
Write a script that adds all arguments
to a Python list, and then save them to a file.
"""


import sys
import json
import os.path


save_to_json_file = __import__("5-save_to_json_file.py").save_to_file
