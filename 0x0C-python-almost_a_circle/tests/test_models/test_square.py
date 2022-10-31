""" Defines tests class for the Square class in square module """
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Test Square attributes and methods """
    def setUp(self):
        """ setup class instances for use in tests """
        self.sqr = Square(5)
        self.sqr1 = Square(5, 5)
        self.sqr2 = Square(5, 0, 0, 14)
        self.sqr3 = Square(5)

    def test_correct_instantiation(self):
        """ should instantiate attributes via Rectangle """
        self.assertEqual(type(self.sqr), Square)

    def test_correct_width_assignment(self):
        """ should instantiate attributes via Rectangle """
        self.assertEqual(self.sqr.width, 5)

    def test_correct_height_assignment(self):
        """ should instantiate attributes via Rectangle """
        self.assertEqual(self.sqr.height, 5)

    def test_validation_inheritance_negative_x(self):
        """ should raise error for invalid value """
        with self.assertRaises(ValueError):
            self.sqr.x = -1

    def test_validation_inheritance_float_y(self):
        """ should raise a ValueError """
        with self.assertRaises(TypeError):
            self.sqr.y = 5.5

    def test_str_overloading(self):
        """ should print str startig with [Square] """
        self.assertEqual(str(self.sqr2), '[Square] (14) 0/0 - 5')

    def test_area_inheritance(self):
        """ should return size ** 2 """
        self.assertEqual(self.sqr.area(), 25)

    def test_size_setter_type_validation_float(self):
        """ should validate size w.r.t type """
        with self.assertRaises(TypeError):
            self.sqr.size = 2.4

    def test_size_setter_type_validation_str(self):
        """ should validate size w.r.t type """
        with self.assertRaises(TypeError):
            self.sqr.size = '2'

    def test_size_setter_value_validation(self):
        """ size value > 0 """
        with self.assertRaises(ValueError):
            self.sqr.size = 0

    def test_update_id(self):
        """ should update object id to specified """
        self.sqr.update(100)
        self.assertEqual(self.sqr.id, 100)

    def test_update_with_args(self):
        """ should update object attrs to specified, in the
        order: id, size, x and y """
        self.sqr.update(78, 20, 30)
        self.assertEqual(self.sqr.size, 20)
        self.assertEqual(self.sqr.x, 30)

    def test_update_kwargs_skipped(self):
        """ should update object attrs to specified, in the
        order: id, size, x and y & kwargs skipped if given"""
        self.sqr.update(78, 20, 30, id=97, size=2, x=4)
        self.assertEqual(self.sqr.id, 78)
        self.assertEqual(self.sqr.size, 20)
        self.assertEqual(self.sqr.x, 30)

    def test_update_with_kwargs(self):
        """ should update object attrs to specified in keyword args"""
        self.sqr.update(x=78, y=20, id=30)
        self.assertEqual(self.sqr.size, 5)
        self.assertEqual(self.sqr.x, 78)

    '''def test_to_dictionary(self):
        """ should return a dictionary rep of an instance
        with all attributes represented """
        the_dict = sorted(self.sqr.to_dictionary())  # a list of keys
        attrs = sorted(['x', 'y', 'size', 'id'])
        idx = 0
        for key in the_dict:
            self.assertEqual(key, attrs[idx])
            idx += 1'''
