#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ Finds all multiples of two(2) in a list
    Args:
        my_list: a list of integers
    Returns:
        A same size list (as my_list) of booleans, True or False
        depending on whether an int at that index is a multiple
        of 2
    """
    # Initialize an empty list for results
    bool_list = []
    for i in my_list:
        bool_list.append(i % 2 == 0)
    return bool_list
