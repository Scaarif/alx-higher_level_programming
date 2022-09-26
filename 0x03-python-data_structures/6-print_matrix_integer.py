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
            if len(row) > 1:
                for i in range(len(row) - 1):
                    print("{:d}".format(row[i]), end=" ")
                # print last element & jump to new row
                print("{:d}".format(row[i + 1]))
            else:
                # print the one element in the row and jump to next row
                print("{:d}".format(row[0]))
    else:
        print()  # print an empty line if matrix empty
