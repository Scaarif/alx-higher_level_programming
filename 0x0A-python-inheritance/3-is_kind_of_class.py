#!/usr/bin/python3
""" Defines a function that returns True if an object
is an instance of the specified class & False otherwise """


def is_kind_of_class(obj, a_class):
    """ returns True if obj is an instance of a_class and
    False otherwise  """
    return isinstance(obj, a_class)
