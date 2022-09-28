#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ Returns a new dictionary with values doubled
    Args:
        a_dictionary: the dict to sort
    Return:
        New dict
    """
    dict = {}
    for k, v in a_dictionary.items():
        dict[k] = v * 2
    return dict
