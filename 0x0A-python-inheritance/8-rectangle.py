#!/usr/bin/python3
""" Defines a class Rectangle that inherits from class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Initializes the class with attributes
        width and height """
        # validate values with super().integer_validator
        values = [('width', width), ('height', height)]
        for value in values:
            super().integer_validator(value[0], value[1])
        self.__height = height
        self.__width = width
