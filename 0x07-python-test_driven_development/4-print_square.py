#!/usr/bin/python3
"""
A simple print square module
Enforces parameter type to integer by raising a TypeError
exception if otherwise
"""


def print_square(size):
    """ Prints a square with the character #
    Also raises a ValueError if size is less than 0
    """
    if type(size) not in [int, float]:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    # Print the square (rows and columns)
    for i in range(int(size)):
        print('#' * int(size))
