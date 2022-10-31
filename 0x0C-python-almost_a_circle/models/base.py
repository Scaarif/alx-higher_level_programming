#!/usr/bin/python3
""" Creating the first class, Base, in the Python Package, models
NOTE:
    a python package is created by including an __init__.py file
    in a folder (the package folder eg this models folder)
"""
import json


class Base:
    """ Defining the class, Base """
    # create a private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor: initializing class instances:
            1. increment the private class attribute __nb_objects
            2. assign a value to id on the basis of whether it is provided
            at object instantiation
        """
        # check if id is provided and assign its value accordingly
        if id:
            self.id = id
        # if not id (i.e.is None), __nb_objects++ & assign that value to id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of a
        list_dictionaries:
        Args:
            list_dictionaries: a list of dictionaries """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"  # otherwise...

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of lisr_objs
        to a file:
        Args:
            list_objs: a list of instances who inherits of Base
            cls: the class of said instances eg Square or Rectangle
        """
        # check if list_objs is provided
        if not list_objs or len(list_objs) == 0:
            list_objs = []
        # save to a file {Class name}.json
        filename = f'{cls.__name__}.json'
        # print(filename)
        with open(filename, mode='w', encoding='utf-8') as f:
            list_dicts = []
            for idx, obj in enumerate(list_objs):
                obj_dict = obj.to_dictionary()
                list_dicts.append(obj_dict)
            json_str = cls.to_json_string(list_dicts)
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation
        of json_string:
        Args:
            json_string: a string rep-ing a list of dictionaries
        """
        # check if json_string is defined
        if not json_string:
            ret_list = []
        ret_list = json.loads(json_string)
        return ret_list
