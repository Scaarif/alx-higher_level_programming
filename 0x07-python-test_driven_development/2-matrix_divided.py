#!/usr/bin/python3
"""
A simple matrix (list of lists) division module
Enforces that a matrix must be a list of lists, each row
must be of the same size and div must be a number (cant be 0)
"""


def matrix_divided(matrix, div):
    """ returns a new matrix of values after member division
    Raises exceptions if the above enforcements aren't adhered to
    """
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists)' \
                ' of integers/floats')
    for row in matrix:
        if (type(row) is not list):
            raise TypeError('matrix must be a matrix (list of lists) '\
                'of integers/floats')
        for elem in row:
            if (type(elem) not in [int, float]):
                raise TypeError('matrix must be a matrix (list of lists) '\
                    'of integers/floats')
    length = len(matrix[0])
    for row in matrix:
        if not (len(row) == length):
            raise TypeError('Each row of the matrix must have the same size')
    if (type(div) not in [int, float]):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        new_matrix = []
        new = []
        for row in matrix:
            for elem in row:
                new.append(round(elem / div, 2))
            new_matrix.append(new)
            new = []  # reset new to empty
        return new_matrix
