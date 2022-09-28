#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Replaces all occurences of an element by another in a new list
    Description:
        Does not modify the list
    Args:
        my_list: the list in which to search for an element
        search: the element to search and replace
        replace: the element to replace search with in new list
    Return:
        the new list
    """
    # Copy my_list
    new = my_list[:]
    if len(new):
        for idx, elem in enumerate(new):
            if elem == search:
                new[idx] = replace
    return new
