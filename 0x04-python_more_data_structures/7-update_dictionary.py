#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ Replaces / adds key/value piars in a dictionary
    Args:
        a_dictionary: the dictionary
        key: a key in a dict (or to add into a dict)
        value: the value to be associated with the key
    Return:
        a new dict (modified)
    """
    a_dictionary[key] = value
    return a_dictionary
