#!/usr/bin/python3
""" *kwargs (keyword arguments) in a nutshell """


def test_var_kwarg(**kwargs):
    """ demonstrates use of **kwargs, which refer to a
    variable no of keyword args to the function
    Args:
        *kwargs: a variable length argument (could be just one
        argument (a pair)  or a dict of them, since they are keyworded
        i.e. a keyword and its value)
    """
    # print the variable length kwargs (could be 1 pair or many)
    for kwarg, value in kwargs.items():
        print("another kwarg through **kwargs :(", kwarg, ":", value, ")")

# test the function...
test_var_kwarg(name='Rahab', lan1='python', lang2='C', lang3='JS')
