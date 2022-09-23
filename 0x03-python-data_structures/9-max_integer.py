#!/usr/bin/python3
def max_integer(my_list=[]):
    """ Returns the biggest integer in a list
    Args:
        my_list: a list of integers
    """
    # Initialize m to first element or None if empty list
    m = my_list[0] if len(my_list) > 0 else None
    for i in my_list:
        m = i if m < i else m
    return m
