#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix
    Description:
        Does not modify the initial matrix, squares each value in it
    Return:
        the new squares matrix
    """
    if len(matrix[0]):
        return [list(map(lambda n: n**2, sublist)) for sublist in matrix]
    return matrix
