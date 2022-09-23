#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ Prints a matrix of integers
    Args:
        matrix: the matrix whose integers to print
    Returns:
        Nothing
    """
    # Determine if matrix is empty, if not -
    if len(matrix[0]) > 0:
        # Access each row in the matrix
        for row in matrix:
            # Access the elements in a row
            for i in range(len(row) - 1):
                print("{}".format(row[i]), end=" ")
            # print last element & jump to new row
            print("{}".format(row[i + 1]))
    else:
        print()  # print an empty line if matrix empty
