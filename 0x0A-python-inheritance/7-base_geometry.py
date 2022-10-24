#!/usr/bin/python3
""" Defines a class BaseGeometry """


class BaseGeometry(object):
    """ create the class """
    def area(self):
        """ raises an exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value which must be an integer and
        >= 0. Raises exceptions otherwise """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        # else:
        #     self.value = value
        # self.name = name
