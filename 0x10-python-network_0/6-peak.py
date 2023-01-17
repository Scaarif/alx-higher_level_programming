#!/usr/bin/python3
""" Defines a function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Return the peak of the list provided
    Note: there may be more than one peak in the list
    """
    # divide the list into 2 and check one sublist
    ls = list_of_integers
    if not len(ls):
        return None
    elif len(ls) == 1:
        return ls[0]
    elif len(ls) == 2:
        if ls[0] > ls[1]:
            return (ls[0])
        else:
            return (ls[1])
    else:
        if (len(ls) % 2):
            mid = len(ls) // 2
        else:
            mid = (len(ls) // 2) - 1
        if len(ls) % 2:  # even (sublists equal)
            # check if the mid value is greater than its neihbours
            if ls[mid - 1] < ls[mid] > ls[mid + 1]:
                return ls[mid]
            else:
                if ls[mid - 1] > ls[mid + 1]:
                    return find_peak(ls[:mid])
                else:
                    return find_peak(ls[mid + 1:])
        else:  # mid is part of first sub list
            if (ls[mid] >= ls[mid + 1]):
                return find_peak(ls[:mid + 1])
            else:
                return find_peak(ls[mid + 1:])


if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3, 7]))
