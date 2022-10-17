#!/usr/bin/python3
""" Creating a class Square """


class Square:
    """ creates a class with a private attribute size """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the instance and enforce the type
        of size to be a positive integer
        """
        self.__size = size
        self.__position = position

    def __repr__(self):
        """ represents the square as #'s (i.e. area characters)
        if size = 0, substitutes an empty line """
        sqr = ''
        if self.__size == 0:
            sqr += '\n'  # rep as an empty line
        else:
            rows = 0
            # if self.__position[1] > 0:
            #     spaces = 0
            # else:
            spaces = self.__position[0]
            blanks = self.__position[1]
            for blank in range(blanks):
                sqr += '\n'
            while (rows < self.__size):
                sqr += ' ' * spaces + '#' * self.__size
                # i = 0
                # while (i < spaces):
                #     sqr += ' '
                #     i += 1
                # cols = 0
                # while (cols < self.__size):
                #     sqr += '#'
                #     cols += 1
                if rows < (self.__size - 1):
                    sqr += '\n'
                rows += 1
        return sqr

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

    @property
    def position(self):
        """ getter for the position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter method for the position attribute """
        # check that position is a 2 positive ints tuple
        if ((type(value) is not tuple) or (len(tuple) != 2)
                or (type(value[0]) is not int) or (type(value[1]) is not int)
                or (value[0] < 0 or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 integers")
        else:
            self.__position = value

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
            # if self.__position[1] > 0:
            #     spaces = 0
            # else:
            spaces = self.__position[0]
            while (rows < self.__size):
                i = 0
                while (i < spaces):
                    print(' ', end="")
                    i += 1
                cols = 0
                while (cols < self.__size):
                    print('#', end="")
                    cols += 1
                if rows < (self.__size - 2):
                    print()
                rows += 1
