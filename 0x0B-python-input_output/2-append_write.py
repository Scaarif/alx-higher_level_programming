#!/usr/bin/python3
""" Defines a function that appends a string to  the end of a text file """


def append_write(filename="", text=""):
    """ appends a string to the end a text file (UTF8)
    and returns the number of characters written(appended) """
    # check that filename  & text is given
    if filename and text:
        # the mode 'a' appends(adds to) the contents of filename
        with open(filename, mode='a', encoding='utf-8') as f:
            # write text into filename & return no of characters written
            return f.write(text)


if __name__ == "__main__":
    # compare no of characters written to those read:
    print(append_write('test2.txt', 'This School is so cool!\n'))
    with open('test2.txt', encoding='utf-8') as f:
        print('chars read:', len(f.read()))
