#!/usr/bin/python3
""" Defines a class Rectangle that inherits from class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Initializes the class with attributes
        width and height """
        # validate values with super().integer_validator
        names = [(width, 'width'), (height, 'height')]
        for name in names:
            super().integer_validator(name[1], name[0])
        self.__height = height
        self.__width = width

    def __str__(self):
        """ returns a formatted Rectangle object """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """ implements area of a Rectangle """
        return self.__width * self.__height
