#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix
    Description:
        Does not modify the initial matrix, squares each value in it
    Return:
        the new squares matrix
    """
    squares = matrix[:]
    print(squares)
    if len(matrix[0]):
        for r in range(len(squares)):
            for i in range(len(squares[r])):
                squares[r][i] = squares[r][i] ** 2
        return squares
    return matrix
