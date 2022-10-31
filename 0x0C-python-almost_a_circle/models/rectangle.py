#!/usr/bin/python3
""" Defines a class, Rectangle, that inherits from class Base """
from models.base import Base


class Rectangle(Base):
    """ Defining the class, Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor: initializing class instance
        & its attributes as well as the super(Base) class
        """
        # private instance attributes first
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # initialize the instance attribute id via the super class' init method
        Base.__init__(self, id)

    # define the getter and setters for the private attributes
    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter: checks that the width value is valid"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ width setter: checks that the width value is valid"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter: checks that the x value is valid"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter: checks that the y value is valid """
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """ returns the area of a Rectangle instance """
        return self.width * self.height  # i.e. the getter values

    def display(self):
        """ prints in stdout the Rectangle instance with the character #.
        Takes care of the x and y values by:
            1. printing y blank lines if y &
            2. printing x spaces if x
        """
        # print y blank lines
        if self.y:
            print('\n' * (self.y - 1))
        # for every row in height, print all columns(width)
        row = 0
        spaces = ' ' * self.x
        row_cols = spaces + '#' * self.width
        while (row < self.height):
            print(row_cols)
            row += 1

    def __str__(self):
        """ Overrides the __str__ method to return the following... """
        return ("[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/"
                + str(self.y) + " - " + str(self.width) + "/"
                + str(self.height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute in the order:
        id, width, height, x & y - i.e. no-keyword arguments
        Alternatively assigns keyword args (**kwargs) if
        *args isn't given or is empty
        """
        # check if args is provided and that args isn't empty
        if args and len(args) > 0:
            args_list = ['id', 'width', 'height', 'x', 'y']
            for idx, arg in enumerate(args):
                setattr(self, args_list[idx], arg)
        # else (if args is empty/ undefined, only then use **kwargs)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """ returns a dictionary representation of a Rectangle """
        attr_dict = getattr(self, '__dict__', None)
        if attr_dict:
            '''attr_list = ['id', 'width', 'height', 'x', 'y']
            ret_dict = {}'''
            new = {}
            for key, value in attr_dict.items():
                '''for name in attr_list:
                    if name == key[(len(key) - len(name)):]:
                        ret_dict[name] = value
                        break'''
                new[key.lstrip('_Rectangle__')] = value
            # print("new", new)
            return new
        return {}
