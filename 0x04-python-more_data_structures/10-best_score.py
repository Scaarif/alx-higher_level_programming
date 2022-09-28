#!/usr/bin/python3
def best_score(a_dictionary):
    """ Returns a key with the biggest integer value
    Args:
        a_dictionary: the dict to sort
    Return:
        a key
    """
    maxi = -1
    maxi_k = None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > maxi:
                maxi = v
                maxi_k = k
    return maxi_k
