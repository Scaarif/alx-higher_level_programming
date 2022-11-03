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
        base = Base()
        self.assertIsInstance(base, Base)

    def test_with_id_instance(self):
        """ should instantiate with an id = 20 """
        base = Base(20)
        self.assertEqual(base.id, 20)
