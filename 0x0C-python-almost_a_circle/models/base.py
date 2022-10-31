#!/usr/bin/python3
""" Creating the first class, Base, in the Python Package, models
NOTE:
    a python package is created by including an __init__.py file
    in a folder (the package folder eg this models folder)
"""


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
