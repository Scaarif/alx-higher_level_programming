#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Prints a sorted dictionary
    Description:
        Sorts only the first level of keys, alphabetically
    Args:
        a_dictionary: the dict to sort
    Return:
        Nothing
    """
    # Get a sorted list of dict keys
    keys = sorted(a_dictionary)
    # Print the sorted dict
    for k in keys:
        print(f"{k}: {a_dictionary[k]}")
