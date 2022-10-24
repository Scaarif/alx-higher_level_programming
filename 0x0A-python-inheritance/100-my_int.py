#!/usr/bin/python3
""" Defines a class my_int that inherits from int <class> """


class MyInt(int):
    """ create a rebel class my_int that inherits from int class """
    def __eq__(self, other):
        """ reverse the operation of == from int class """
        return (self - other) != 0

    def __ne__(self, other):
        """ reverse the operation of == from int class """
        return (self - other) == 0
