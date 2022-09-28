#!/usr/bin/python3
def weight_average(my_list=[]):
    """ Returns the weighted average of all integer tuples
    Args:
        my_list: a list of 2 ints tuples
    Return:
        the weighted average computed
    """
    # get each tuple in list
    avg = 0
    product_sum = 0
    _2nd_sum = 0
    if len(my_list):
        for tpl in my_list:
            product_sum += tpl[0] * tpl[1]
            _2nd_sum += tpl[1]
        avg = product_sum / _2nd_sum
    return avg
