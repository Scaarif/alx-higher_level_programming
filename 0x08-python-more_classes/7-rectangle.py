#!/usr/bin/python3
""" Defines a class that creates/defines a Rectangle """


class Rectangle:
    """ Defines attributes, class and instance """
    # create a public attribute
    number_of_instances = 0
    # and another -  for use in str rep (str)
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize a class instance with attributes """
        self.__width = width
        self.__height = height
        # increment the class attr on each instantiation
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for the width (private) instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width attribute """
        # check that value is an integer & positive
        if type(value) not in [int, float]:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for the height (private) instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the height attribute """
        # check that value is an integer & positive
        if type(value) not in [int, float]:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >=0')
        else:
            self.__height = value

    def perimeter(self):
        """ Returns the perimeter of a rectangle """
        # check that neither width nor height is 0
        if self.width == 0 or self.height == 0:
            return 0
        # return the perimeter otehrwise
        return 2 * (self.width + self.height)  # property(s)

    def area(self):
        """ returns the area of a rectangle """
        return self.width * self.height

    # define some magic methods
    def __str__(self):
        """ returns the rectangle as a '#' diagram """
        # check that neither height nor width is 0
        if self.width == 0 or self.height == 0:
            return ''
        # return the rectangle (rep by '#')
        rect = ''
        for row in range(self.height):
            # I initially used Rectangle.print_symbol - but that then only
            # applied if str was called against Rectangle, not an instance
            # i.e. with instance.print_symbol = '&' and the class var
            # print_symbol = '#', '#' is printed, instead of '&' since the
            # former creates a new instance of the var,
            # it doesn't update the global var (which I was calling here!)
            rect += str(self.print_symbol) * self.width
            if row < (self.height - 1):
                rect += '\n'
        return rect

    def __repr__(self):
        """ returns an eval() capable representation of an object """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """ deletes this class instance """
        # decrement number_of_instances
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
