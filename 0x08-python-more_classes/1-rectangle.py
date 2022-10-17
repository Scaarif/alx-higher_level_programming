#!/usr/bin/python3
""" Defines a class that creates/defines a Rectangle """


class Rectangle:
    """ create the class Rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize a class instance with attributes """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for the width (private) instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width attribute """
        # check that value is an integer & positive
        if type(value) not in [int, float]:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for the height (private) instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the height attribute """
        # check that value is an integer & positive
        if type(value) not in [int, float]:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >=0')
        else:
            self.__height = value
