#!/usr/bin/python3
""" Defines a function that inserts a line of test to a file
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text (new_string) after a line, if the line
    contains the search_str """
    # check that the filename and the other args are provided
    if filename and search_string and new_string:
        new_file_txt = ""
        with open(filename, encoding='utf-8') as f:
            # search the search_string in f
            while True:
                line = f.readline()
                if line:
                    new_file_txt += line
                    if search_string in line:
                        new_file_txt += new_string
                else:
                    break
        # write the new contents to the file
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(new_file_txt)
