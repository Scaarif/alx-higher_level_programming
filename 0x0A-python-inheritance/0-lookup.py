#!/usr/bin/python3
""" Defines a function that returns a list of available
attributes & methods of an object """


def lookup(a_object):
    """ returns the available attributes and methods
    of  a_object """
    return dir(a_object)
