#!/usr/bin/python3
def remove_char_at(str, n):
    """ Returns a copy of str with the character at n removed """
    if n < 0:
        return str
    else:
        return str[:n] + str[n + 1:]
