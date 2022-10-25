#!/usr/bin/python3
""" Defines a function that writes to a JSON file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a JSON file """
    # check that filename  & object are given
    # if filename and my_obj:
    # the mode 'w' overwrites the contents of filename if in existence
    with open(filename, mode='w', encoding='utf-8') as f:
        # dump(write) the object into filename
        json.dump(my_obj, f)
