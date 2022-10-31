""" Defines tests for the Rectangle class in rectangle module
<rectangle.py> """
from models.rectangle import Rectangle
import unittest


class TestRectangleClass(unittest.TestCase):
    """ Create a class with tests for the Rectangle class """
    def test_zero_args_instance(self):
        """ should fail to instantiate, positional args:
        width & height required """
        with self.assertRaises(Exception):
            rect = Rectangle()

    def test_valid_instance(self):
        """ should instantiate, positional args provided """
        rect = Rectangle(2, 2)
        self.assertEqual(rect.width, 2)

    def test_instance_inheritance(self):
        """ should return correct id values, w.r.t whether id is defined """
        rect1 = Rectangle(2, 2)
        rect2 = Rectangle(2, 2)
        rect3 = Rectangle(2, 2)
        rect4 = Rectangle(2, 2, 1, 1, 10)
        rect5 = Rectangle(2, 2, 1, 1)
        self.assertEqual(rect1.id, 2)
        self.assertEqual(rect2.id, 3)
        self.assertEqual(rect3.id, 4)
        self.assertEqual(rect4.id, 10)
        self.assertEqual(rect5.id, 5)

    def test_invalid_float_width(self):
        """ should raise an exception - TypeError """
        with self.assertRaises(TypeError):
            rect = Rectangle(2.5, 7)

    def test_invalid_zero_width(self):
        """ should raise an exception - ValueError """
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 0)

    def test_invalid_float_height(self):
        """ should raise an exception - TypeError """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 7.0)

    def test_invalid_zero_height(self):
        """ should raise an exception - TypeError """
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 0)

    def test_invalid_negative_height(self):
        """ should raise an exception - ValueError """
        with self.assertRaises(ValueError):
            rect = Rectangle(2, -1)

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
            rect = Rectangle(2, 2, -2)

    def test_invalid_negative_y(self):
        """ should raise an exception - ValueError """
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 2, 0, -2)

    def test_invalid_string_width(self):
        """ should raise an exception - TypeError"""
        rect = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            rect.width = '12'

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
