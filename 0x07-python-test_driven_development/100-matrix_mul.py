#!/usr/bin/python3
""" A matrix multiplication module
Multiplies two matrices with the folling requirements:
    1. each must be a list of lists
    2. both must be rectangular
    3. must be made up of purely numbers (ints &/ floats)
"""


def matrix_mul(m_a, m_b):
    """ Returns a matrix - the product of the two matrices
    Raises exceptions if any of the requrements above aren't met
    """
    # Check that both matrices are lists and contain lists
    lists = [m_a, m_b]
    names = ['m_a', 'm_b']
    for idx, a_list in enumerate(lists):
        # check that a matrix is a list
        if type(a_list) is not list:
            raise TypeError(f'{names[idx]} must be a list')
        # check that a matrix is not empty
        if len(a_list) == 0:
            raise ValueError(f'{names[idx]} can\'t be empty')
        # check that a matrix is a list of lists
        for elem in a_list:
            if type(elem) is not list:
                raise TypeError(f'{names[idx]} must be a list of lists')
            # check that all elements are ints/floats
            for char in elem:
                if type(char) not in [int, float]:
                    raise TypeError(f'{names[idx]} should contain only \
                    integers or floats')
            # check that each row (elem) has the same no of cols(char)
            d_cols = len(a_list[0])  # get the first row's cols if list
            r_cols = len(elem)  # no of cols in a row
            if r_cols != d_cols:
                raise TypeError(f'each row of {names[idx]} must be of the \
                same size')
    # check that the matrices can be multiplied
    rows = len(m_b)
    cols = len(m_a[0])
    if rows != cols:
        raise ValueError('m_a and m_b can\'t be multiplied')
    # perform the multiplication
    res = []  # to hold the new matrix
    for row in m_a:
        res_row = []
        for b_col in range(len(m_b[0])):  # simulate a cols traverser in m_b
            # get a value to append to res_row
            prod_sum = 0
            col_row = 0
            for elem in row:
                prod_sum += elem * m_b[col_row][b_col]
                col_row += 1
            res_row.append(prod_sum)
            prod_sum = 0  # reset value
        res.append(res_row)
        res_row = []  # reset to empty
    return res


if __name__ == "__main__":
    mat = [[1, 2], [2, 2]]
    print(matrix_mul(mat, mat))
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
