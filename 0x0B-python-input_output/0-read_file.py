#!/usr/bin/python3
""" Defines a function that reads a text file and prints it
to stdout """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """
    # check that filename is given
    if filename:
        with open(filename, encoding='utf-8') as f:
            # print out the contents read
            print(f.read(), end="")
            # Note: the end="" prevents addition of an extra line
