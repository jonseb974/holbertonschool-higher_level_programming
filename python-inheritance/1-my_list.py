#!/usr/bin/python3
# 1-my_list.py
"""Inherits
"""


class MyList(list):
    """class that inherits from list.
    """
    def print_sorted(self):
        """Public instance method
        prints the list in ascending sort.
        """
        print(sorted(self))
