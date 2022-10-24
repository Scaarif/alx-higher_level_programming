#!/usr/bin/python3
""" Defines a function adds a new attribute to an object if its possible  """


def add_attribute(obj, name, value):
    """ adds an attribute to a class if possible  """
    # check that the attribute doesn't exist
    exists = getattr(obj, "__doc__", None)
    # if not, add the attribute
    if exists is None:
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
