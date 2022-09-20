#!/usr/bin/python3
def print_last_digit(number):
    """ Prints the last digit in a number """
    # provide for negative numbers
    if number < 0:
        number *= -1
    print(number % 10, end="")
    return number % 10
