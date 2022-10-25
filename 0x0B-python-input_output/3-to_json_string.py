#!/usr/bin/python3
""" Defines a function that serializes a python object """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of a Python object (serializes) """
    return json.dumps(my_obj)
