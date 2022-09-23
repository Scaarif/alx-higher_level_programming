#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ Adds 2 tuples
    Args:
        tuple_a: first tuple
        tuple_b: second tuple
    Description:
        adds the elements at same indices in the two tuples together
        substitutes for an empy element with 0 in either tuple
    Returns:
        a tuple of the result of summation
    """
    # Add up the elements
    ans = []
    # handle tuples of length 0 and 1
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    len_ = len(tuple_a) if len(tuple_a) > len(tuple_b) else len(tuple_b)
    for i in range(len_):
        sum_ = (tuple_a[i] + tuple_b[i])
        ans.append(sum_)
    return ans[0], ans[1]
