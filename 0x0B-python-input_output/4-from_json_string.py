#!/usr/bin/python3
""" Defines a function that deserializes a JSON object """
import json


def from_json_string(my_str):
    """ returns a Python object represented by a
    JSON string (deserializes the string) """
    return json.loads(my_str)
