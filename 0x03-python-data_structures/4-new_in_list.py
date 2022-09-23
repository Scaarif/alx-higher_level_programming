#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ Replaces element at idx with element in a copy of that list the C way
    Args:
        my_list: the list
        idx: index of the element to replace
        element: the element to replace the old with
    Description:
        Returns a copy of original list if idx is out of range or negative
        and a copy of the new list otherwise
    """
    if idx > (len(my_list) - 1) or idx < 0:
        # Return a copy of the original list
        return my_list[:]
    else:
        # make a copy of the original and modify its value
        list_copy = my_list[:]
        list_copy[idx] = element
        return list_copy
