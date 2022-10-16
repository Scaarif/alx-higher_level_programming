#!/usr/bin/python3
"""
A simple string concatenation module
Enforces parameter types to strings by raising a TypeError
exception if otherwise
"""


def say_my_name(first_name, last_name=""):
    """ returns a string with the args concatenated into a full name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    string = 'My name is ' + first_name + ' ' + last_name
    print(string)
