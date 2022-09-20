#!/usr/bin/python3
def remove_char_at(str, n):
    """ Returns a copy of str with the character at n removed """
    if n < 0:
        return str # Turns out C does not support negative indices
    else:
        return str[:n] + str[n + 1:]
