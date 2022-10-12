#!/usr/bin/python3
""" Creating a class Square """


class Square:
    """ creates an a class with a private attribute size """
    def __init__(self, size=0):
        """ Initialize the instance and enforce the type
        of size to be a positive integer
        """
        # check that size is an int and raise an exception if not
        if type(size) is not int:
            raise TypeError("size must be an integer")
        # check that the value is >= 0, raise an exception otherwise
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ returns the area of a square """
        return self.__size ** 2
