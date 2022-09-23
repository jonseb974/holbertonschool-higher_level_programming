#!/usr/bin/python3
"""Module to find the max integer in a list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular(self):
        """Test with regular list of int: return Max value """
        list_reg = [1, 2, 3, 4]
        result = max_integer(list_reg)
        self.assertEqual(result, 4)

    def max_integer(self):
        """Test if list is empty """
        list_int = []
        result = max_integer
        self.assertEqual(result, None)

    def max_integer(self):
        """Test value float list: Return max """
        list_float = [1.5, 5.5, 2.5]
        result = max_integer(list_float)
        self.assertEqual(result, 5.5)

    def max_integer(self):
        """Test value of int list: Return max """
        list_int = [1, 5, 2]
        result = max_integer(list_int)
        self.assertEqual(result, 5)

    def max_begining(self):
        """Test if max value at the begining: Return Max """


if __name__ == '__main__':
    unittest.main()
