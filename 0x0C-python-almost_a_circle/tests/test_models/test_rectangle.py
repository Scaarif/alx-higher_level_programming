#!/usr/bin/python3
""" Defines tests for the Rectangle class in rectangle module
<rectangle.py> """
from models.rectangle import Rectangle
from models.base import Base
import unittest
import io
import sys


class TestRectangleClass(unittest.TestCase):
    """ Create a class with tests for the Rectangle class """
    def setUp(self):
        """ setup class instances for use in tests """
        self.rect = Rectangle(5, 5)
        self.rect1 = Rectangle(5, 6, 1, 0)

    def test_valid_instance_2_args(self):
        """ should instantiate, positional args provided """
        rect = Rectangle(2, 2)
        self.assertIsInstance(rect, Base)

    def test_valid_instance_3_args(self):
        """ should instantiate, positional args provided """
        rect = Rectangle(2, 2, 3)
        rect1 = Rectangle(2, 2, 1)
        self.assertTrue(rect.id, rect1.id - 1)

    def test_valid_instance_4_args(self):
        """ should instantiate, positional args provided """
        rect = Rectangle(2, 2, 1, 1)
        rect1 = Rectangle(2, 2, 1, 1)
        self.assertTrue(rect.id, rect1.id - 1)

    def test_zero_args_instance(self):
        """ should fail to instantiate, positional args:
        width & height required """
        with self.assertRaises(Exception):
            rect = Rectangle()

    def test_instance_inheritance(self):
        """ should return correct id values, w.r.t whether id is defined """
        rect4 = Rectangle(2, 2, 1, 1, 10)
        self.assertEqual(rect4.id, 10)

    def test_valid_x(self):
        """ should instantiate, update x to 2 """
        rect = Rectangle(2, 2, 2)
        self.assertEqual(rect.x, 2)

    def test_valid_y(self):
        """ should instantiate, update y to 2 """
        rect = Rectangle(2, 2, 2, 2)
        self.assertEqual(rect.y, 2)

    def test_invalid_negative_x(self):
        """ should raise an exception - ValueError """
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 2, -1, 4)

    def test_invalid_negative_y(self):
        """ should raise an exception - ValueError """
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 2, 0, -2)

    def test_invalid_string_x(self):
        """ should raise an exception - TypeError """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 2, '1', 4)

    def test_invalid_string_y(self):
        """ should raise an exception - TypeError """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 2, 0, '2')

    def test_area(self):
        """ should return width * height """
        rect = Rectangle(2, 2)
        self.assertEqual(rect.area(), 4)

    def test_str(self):
        """ should return a formatted string """
        rect = Rectangle(4, 6, 2, 1, 12)
        rect1 = Rectangle(5, 5, 1, 0, 10)
        self.assertEqual(str(rect), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(rect1), '[Rectangle] (10) 1/0 - 5/5')

    def test_update_id(self):
        """ should update object id to specified """
        rect = Rectangle(2, 2)
        rect.update(78)
        self.assertEqual(rect.id, 78)

    def test_update_with_args(self):
        """ should update object attrs to specified, in the
        order: id, width, height, x and y """
        rect = Rectangle(2, 2)
        rect.update(78, 20, 30)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)

    def test_update_kwargs_skipped(self):
        """ should update object attrs to specified, in the
        order: id, width, height, x and y """
        rect = Rectangle(2, 2)
        rect.update(78, 20, 30, id=97, width=2, height=4)
        self.assertEqual(rect.id, 78)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)

    def test_update_with_kwargs(self):
        """ should update object attrs to specified in keyword args"""
        rect = Rectangle(2, 2)
        rect.update(x=78, y=20, id=30)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.x, 78)

    def test_to_dictionary(self):
        """ should return a dictionary rep of an instance
        with all attributes represented """
        rect = Rectangle(2, 2)
        the_dict = sorted(rect.to_dictionary())
        attrs = sorted(['x', 'y', 'width', 'height', 'id'])
        idx = 0
        for key in the_dict:
            self.assertEqual(key, attrs[idx])
            idx += 1

    # Setup for testing display method
    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on rect.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangleClass.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangleClass.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangleClass.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangleClass.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)
