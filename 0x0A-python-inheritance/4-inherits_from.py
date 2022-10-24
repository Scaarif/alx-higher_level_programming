#!/usr/bin/python3
""" Defines a function that returns True if an object
is an instance of a class that inherited from the specified class
(directly or indirectly) & False otherwise """


def inherits_from(obj, a_class):
    """ returns True if obj is an instance of a_class (by
    direct or indirect inheritance) and
    False otherwise  """
    if isinstance(obj, a_class):
        return not issubclass(a_class, type(obj))
