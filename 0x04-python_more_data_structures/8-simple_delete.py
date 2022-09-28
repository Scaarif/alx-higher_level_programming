#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ Deletes a key/value pair in a dictionary
    Args:
        a_dictionary: the dictionary
        key: a key to delete from a dict (+ value)
    Return:
        a new dict (modified)
    """
    # check that key is in a_dict before calling del - avoid KeyError
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
