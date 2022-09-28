#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Deletes a key/value pair in a dictionary
    Args:
        a_dictionary: the dictionary
        value: the value to delete from a dict (+ key)
    Description:
        value is searched in the dict, all occurences of it deleted,
        and if a value doesnt exist, nothing happens
    Return:
        a new dict (modified)
    """
    # loop through dict checking for value & call calling del if found
    keys = []
    for k, v in a_dictionary.items():
        if v == value:
            keys.append(k)
    if len(keys):
        for k in keys:
            del a_dictionary[k]
    return a_dictionary
