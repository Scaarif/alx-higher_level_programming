#!/usr/bin/python3
""" *args in a nutshell """


def test_var_arg(f_arg, *argv):
    """ demonstrates use of *args, which refer to a
    variable no of args to the function
    Args:
        f_arg: a normal(required positional) argument to the function
        *argv: a variable length argument (could be just one
        argumen or a list of them)
    """
    # print the positional argument 9normal arg)
    print("first normal arg:", f_arg)
    # print the variable length args (could be 1 or many)
    for arg in argv:
        print("another arg thrugh *argv :", arg)

# test the function...
test_var_arg('Rahab', 'python', 'C', 'JS')
