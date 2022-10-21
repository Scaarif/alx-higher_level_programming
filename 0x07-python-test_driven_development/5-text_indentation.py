#!/usr/bin/python3
"""
A simple text 'formatting' module
Enforces parameter type to string by raising a TypeError
exception if otherwise
"""


def text_indentation(text):
    """ Prints a text with 2 lines after each of the characters:
    ., ? and :
    Raises a TypeError if text is not string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    # Print the text with the additional lines
    flags = ['.', '?', ':']
    len_ = 0
    skip = 0
    length = len(text)
    for char in text:
        if char in flags:
            print(char)
            print()
            len_ += 1
            # Skip the space character(s) right after a flag
            if len_ < length:
                while (text[len_] == ' '):
                    skip += 1
                    len_ += 1
        else:
            if (skip):
                while(skip):
                    skip -= 1
            else:
                print(char, end="")
            len_ += 1
