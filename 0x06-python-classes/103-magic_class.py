#!/usr/bin/python3
import math


class MagicClass:
    """ creates a class """
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        # else
        self.__radius = radius

    def area(self, radius):
        """ returns the area """
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """ returns the circumference """
        return self.__radius * 2 * math.pi
