#!/usr/bin/python3
""" Creating a class Square """


class Square:
    """ creates a class with a private attribute size """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the instance and enforce the type
        of size to be a positive integer
        """
        self.__size = size

    @property
    def size(self):
        """ size getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter method with type and value enforcement
        args:
            value: the size parameter in __init__
        """
        # check that size is an int and raise an exception if not
        if type(value) is not int:
            raise TypeError("size must be an integer")
        # check that the value is >= 0, raise an exception otherwise
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the area of a square """
        return self.__size ** 2

    # define the comparators - as magic methods
    def __lt__(self, other):
        """ answer to less than other """
        return self.__size < other.size

    def __le__(self, other):
        """ answer to less than or equal to other """
        return self.__size <= other.size

    def __eq__(self, other):
        """ answer to equal other """
        return self.__size == other.size

    def __ne__(self, other):
        """ answer to not equal other """
        return self.__size != other.size

    def __gt__(self, other):
        """ answer to greater than other """
        return self.__size > other.size

    def __ge__(self, other):
        """ answer to greater than or equal to other """
        return self.__size >= other.size
