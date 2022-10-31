#!/usr/bin/python3
""" Defines a class Square, a special Rectangle. The class
therefore inherits from the class Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square, that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes Square class instances & attributes """
        # all attributes are initialized from the Rectangle class
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ overloads the Rectangle __str__ method """
        # self.size == self.width or self.height
        return ("[Square] (" + str(self.id) + ") " + str(self.x)
                + "/" + str(self.y) + " - " + str(self.width))

    @property
    def size(self):
        """ size getter """
        return Rectangle.width

    @size.setter
    def size(self, size):
        """ size setter: assigns the width and height with the same
        value. Has the same value validation as Rectangle width and height
        setters """
        # validate the size value
        if type(size) is not int:
            raise TypeError('width must be an integer')
        elif size <= 0:
            raise ValueError('width must be > 0')
        else:
            # assign the value of width & height respectively
            Rectangle.width = size
            Rectangle.height = size

    def update(self, *args, **kwargs):
        """ assigns values to an instance of a class' attributes """
        if args and len(args) > 0:
            attr_list = ('id', 'size', 'x', 'y')
            for idx, arg in enumerate(args):
                setattr(self, attr_list[idx], arg)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a square """
        attrs = getattr(self, '__dict__', None)
        if attrs:
            return_dict = {}
            for key, value in attrs.items():
                # idx = key.index('__') + 2
                return_dict[key.lstrip('_Rectangle__')] = value
            return return_dict
        return {}
