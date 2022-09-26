#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Prints the integers of a list in reverse
    Args:
        my_list: the list of integers
    """
    # Handle the empty list case
    if len(my_list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
    else:
        # list empty - print nothing
        print()
