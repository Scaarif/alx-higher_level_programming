#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list & only integers
    args:
        my_list: list of elements
        x: number of elements to print, could be greater than len(my_list)
    Return: the number of elements printed
    """
    j = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except (TypeError, ValueError):
            continue
    print()
    return j
