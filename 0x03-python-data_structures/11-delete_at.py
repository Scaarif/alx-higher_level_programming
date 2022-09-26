#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ Deletes the element at index idx in a list
    Args:
        my_list: a list of integers
        idx: index of the element to delete
    Returns:
        The modified list
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        del my_list[idx]
        return my_list
