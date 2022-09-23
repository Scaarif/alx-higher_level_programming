#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ Replaces list element at idx with new element the C way
    Args:
        my_list: the list
        idx: index of the element to replace
        element: the element to replace the old with
    Description:
        Returns original list if idx is out of range or negative
    """
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
