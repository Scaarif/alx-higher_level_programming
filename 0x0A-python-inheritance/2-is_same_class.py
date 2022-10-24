#!/usr/bin/python3
""" Defines a function that returns True if an object
is exactly an instance of the specified class & False otherwise """


def is_same_class(obj, a_class):
    """ returns True if obj is, exactly, an instance of a_class and
    False otherwise  """
    return type(obj) == a_class
