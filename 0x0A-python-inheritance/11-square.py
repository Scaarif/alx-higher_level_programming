#!/usr/bin/python3
""" Defines a class Square that inherits from class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle """
    def __init__(self, size):
        """ Initializes the class with attribute size """
        # explicitly initialize Rectangle
        Rectangle.__init__(self, size, size)
        # validate size with super().integer_validator
        super().integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """ format Square object """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

    def area(self):
        """ implements area of a Square """
        return self.__size ** 2
