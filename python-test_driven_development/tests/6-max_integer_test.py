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

    def test_list_integer(self):
        """Test value of int list: Return max """
        list_int = [1, 5, 2]
        result = max_integer(list_int)
        self.assertEqual(result, 5)

    def test_list_begining(self):
        """Test if max value at the begining: Return Max """
        list_int = [10, 9, 8, 7]
        result = max_integer(list_int)
        self.assertEqual(result, 10)

    def test_list_negative(self):
        """Test if value are negative """
        list_int = [-1, -2, -5]
        result = max_integer(list_int)
        self.assertEqual(result, -1)

    def test_list_one_neg(self):
        """Test if one value is negative """
        list_int = [10, -5, 2, 8]
        result = max_integer(list_int)
        self.assertEqual(result, 10)

    def test_list_empty(self):
        list_empty = []
        result = max_integer(list_empty)
        self.assertEqual(result, None)

    def test_list_of_one(self):
        list_int = [5]
        result = max_integer(list_int)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
