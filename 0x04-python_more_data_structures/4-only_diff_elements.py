#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ Returns a set of all elements in only one set
    Args:
        set_1: first set
        set_2: second set
    Return:
        elements in only one set
    """
    return set_1 ^ set_2
