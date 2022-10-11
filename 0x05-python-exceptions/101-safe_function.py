#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function, fct, safely
    args
        fct: function to execute
        args: optional arguments?
    Return: result of the function if executed and None otherwise
    """
    try:
        return fct(*args)
    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return None
