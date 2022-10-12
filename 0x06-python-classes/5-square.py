#!/usr/bin/python3
""" Creating a class Square """


class Square:
    """ creates an a class with a private attribute size """
    def __init__(self, size=0):
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

    def my_print(self):
        """ prints the square as #'s (i.e. area characters)
        if size = 0, prints an empty line """
        if self.__size <= 0:
            print()
        else:
            rows = 0
            while (rows < self.__size):
                cols = 0
                while (cols < self.__size):
                    print('#', end="")
                    cols += 1
                print()
                rows += 1
