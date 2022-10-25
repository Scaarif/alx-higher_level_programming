#!/usr/bin/python3
""" Defines a function that inserts a line of test to a file
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text (new_string) after a line, if the line
    contains the search_str """
    # check that the filename and the other args are provided
    if filename and search_string and new_string:
        with open(filename, mode='r+', encoding='utf-8') as f:
            # search the search_string in f
            while True:
                line = f.readline()
                if line:
                    if search_string in line:
                        offset = f.tell()
                        f.seek(offset, 0)  #go to the offset
                        f.write(new_string)
                else:
                    break
