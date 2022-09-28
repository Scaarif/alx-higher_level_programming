#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix
    Description:
        Does not modify the initial matrix, squares each value in it
    Return:
        the new squares matrix
    """
    new = matrix.copy()

    for i in range(len(matrix)):
        new[i] = list(map(lambda x: x**2, matrix[i]))

    return (new)
