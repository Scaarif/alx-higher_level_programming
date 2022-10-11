#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """prints an integer with "{:d}".format()
    args
        value: (potential)integer, could be of any type
    Return: True if printed and False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return False
