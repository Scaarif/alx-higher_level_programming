#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests for the max_integer function """
    def test_empty_list(self):
        """ Is the return value None given an empty list? """
        res = max_integer([])
        self.assertEqual(res, None)

    def test_ints_list(self):
        """ Does the function work correctly with an ints list? """
        res = max_integer([5, 2, 4, 6, 8])
        self.assertEqual(res, 8)

    def test_list_with_floats(self):
        """ Does the function work correctly with a ints & floats list? """
        res = max_integer([2, 4.5, 1.1, 6.7])
        self.assertEqual(res, 6.7)

    def test_list_with_strings(self):
        """ Does the function raise an error if list contains
        invalid type - say, a string? """
        with self.assertRaises(TypeError):
            max_integer(['test', 3, 2])
