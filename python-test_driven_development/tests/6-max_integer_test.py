#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test """
    def test_regular(self):
        """Test with regular list of int: return Max value """
        list_reg = [1, 2, 3, 4]
        result = max_integer(list_reg)
        self.assertEqual(result, 4)

    def test_list_float(self):
        """Test value float list: Return max """
        list_float = [1.5, 5.5, 2.5]
        result = max_integer(list_float)
        self.assertEqual(result, 5.5)

    def list_integer(self):
        """Test value of int list: Return max """
        list_int = [1, 5, 2]
        result = max_integer(list_int)
        self.assertEqual(result, 5)

    def list_begining(self):
        """Test if max value at the begining: Return Max """
        list_int = [10, 9, 8, 7]
        result = max_integer(list_int)
        self.assertEqual(result, 10)

    def list_integer(self):
        """Test if value are negative """
        list_int = [-1, -2, -5]
        result = max_integer(list_int)
        self.assertEqual(result, -1)

    def list_integer(self):
        """Test if one value is negative """
        list_int = [10, -5, 12, 8]
        result = max_integer(list_int)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
