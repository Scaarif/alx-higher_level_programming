#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Adds all unique integers in a list
    Args:
        my_list: the list of elements
    Return:
        the sum
    """
    sum_ = 0
    if len(my_list):
        uniq = set(my_list)
        for i in uniq:
            sum_ += i
        return sum_
    return sum_
