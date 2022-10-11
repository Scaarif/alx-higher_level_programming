#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()
    args
        value: (potential)integer, could be of any type
    Return: True if printed and False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
