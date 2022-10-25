#!/usr/bin/python3
""" Defines a function that writes to a text file """


def write_file(filename="", text=""):
    """ writes to a text file (UTF8) and returns the number
    of characters written """
    # check that filename  & text is given
    if filename and text:
        # the mode 'w' overwrites the contents of filename if in existence
        with open(filename, mode='w', encoding='utf-8') as f:
            # write text into filename & return no of characters written
            return f.write(text)
