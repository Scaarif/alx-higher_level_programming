#!/usr/bin/python3
""" Defines tests for the base module <base.py> """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBaseClass(unittest.TestCase):
    """ Create a class with tests for the Base class """
    def test_zero_args_instance(self):
        """ should instantiate since id has a default value, 0 """
        b = Base()
        b1 = Base()
        self.assertEqual(b.id, 10)
        self.assertEqual(b1.id, 11)


    def test_with_id_instance(self):
        """ should instantiate with an id = 20 """
        base = Base(20)
        self.assertEqual(base.id, 20)

    def test_excess_args_instance(self):
        """ shouldn't instantiate with excess args """
        with self.assertRaises(Exception):
            base = Base(20, 2)

    def test_to_json_string_type(self):
        """ should return a json string rep of a list of
        instance dictionaries """
        rect = Rectangle(10, 7, 2, 8, 1)
        the_dict = rect.to_dictionary()
        json_dict = Base.to_json_string(the_dict)
        self.assertEqual(type(json_dict), str)

    def test_to_json_string(self):
        """ should return a json string rep of a list of
        instance dictionaries """
        rect = Rectangle(10, 7, 2, 8, 1)
        the_dict = rect.to_dictionary()
        json_dict = Base.to_json_string(the_dict)  # staticmethod
        str_ = '{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}'
        self.assertEqual(sorted(json_dict), sorted(str_))

    def test_save_to_file(self):
        """ should write to a file, <class name>.json - file wont be empty """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) > 0)

    '''def test_save_to_file_overwrite(self):
        """ should overwrite content in <class name>.json """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) > 0)'''

    def test_from_json_string(self):
        """ should return the original string, from which
        the json string's derived """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_from_json_string_empty(self):
        """ should return a empty list """
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_create_different_objects(self):
        """ should return fully instantiated, separate objects """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)

    def test_create_objects(self):
        """ should return fully instantiated object """
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 3/5')

    '''def test_load_from_file_unknown(self):
        """ should return an empty list if file not found """
        list_rectangles_output = Square.load_from_file()
        self.assertTrue(len(list_rectangles_output) == 0)'''

    def test_load_from_file_valid(self):
        """ should return a legit instance should the file be found """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for square in list_squares_output:
            self.assertIsInstance(square, Square)
