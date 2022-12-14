#!/usr/bin/python3
""" creating a class """
import math


class MagicClass:
    """ creates a class """
    def __init__(self, radius=0):
        # self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        # else
        self.__radius = radius

    def area(self):
        """ returns the area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ returns the circumference """
        return self.__radius * 2 * math.pi
