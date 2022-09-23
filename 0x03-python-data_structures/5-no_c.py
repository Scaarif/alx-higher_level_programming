#!/usr/bin/python3
def no_c(my_string):
    """ Removes all characters c and C from my_string
    Args:
        my_string: the string to modify
    Returns:
        the new string (with all c's and C's removed)
    """
    return my_string.translate({ord(c): None for c in 'cC'})
