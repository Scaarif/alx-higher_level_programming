#!/usr/bin/python3
def element_at(my_list, idx):
    """ Retrieves an element from a list the C way
    Args:
        my_list: the list
        idx: index of the element to retrieve
    Description:
        Returns None if idx is out of range or negative
    """
    if idx > (len(my_list) - 1) or idx < 0:
        return None
    else:
        return my_list[idx]
