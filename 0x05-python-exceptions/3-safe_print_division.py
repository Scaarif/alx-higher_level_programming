#!/usr/bin/python3
def safe_print_division(a, b):
    """divides two integers and prints the result
    args:
        a: first integer
        b: second integer
    Return: the result of the dision and None otherwise (on failure)
    """
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        res = None
        return res
    finally:
        print("Inside result: {}".format(res))
