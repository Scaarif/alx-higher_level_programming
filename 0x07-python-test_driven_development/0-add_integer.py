#!/usr/bin/python3
""" A simple module """


def add_integer(a, b=98):
    """ adds 2 integers and raises a TypeError if any of the
    arguments provided is not a float or int
    """
    if a is None or type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
