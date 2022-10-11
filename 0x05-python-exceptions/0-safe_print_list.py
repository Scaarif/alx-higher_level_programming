#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list
    args:
        my_list: list of elements
        x: number of elements to print, could be greater than len(my_list)
    Return: the number of elements printed
    """
    i = 0
    try:
        for elem in my_list:
            if (i < x):
                print(elem, end="")
                i += 1
        print()  # prints a new line
        return (i)
    except IndexError:
        return (0)
