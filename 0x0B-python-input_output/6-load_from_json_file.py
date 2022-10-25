#!/usr/bin/python3
""" Defines a function that creates an object from a JSON file """
import json


def load_from_json_file(filename):
    """ loads an object from a JSON file """
    with open(filename, encoding='utf-8') as f:
        # load (deserialize)
        return json.load(f)
