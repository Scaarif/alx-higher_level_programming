#!/usr/bin/python3
"""Defines a locked class - one that allows only one
dynamically creatable instance attribute, 'first_name' """


class LockedClass:
    """
    Prevent the user from dynamically creating an instance attribute
    unless the attribute's called 'first_name'.
    """

    __slots__ = ["first_name"]
