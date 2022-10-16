#!/usr/bin/python3
""" A replication of the matrix multiplication module,
100-matrix_mul.py, using Numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ returns the matrix product, a matrix """
    # check the matrices:
    # matrices = [m_a, m_b]
    # names = ['m_a', 'm_b']
    # for idx, matrix in enumerate(matrices):
    #     # check that each arg is a matrix (2-d) array
    #     if matrix.ndim != 2:
    #         raise TypeError(f'{names[idx]} must be a matrix')
    #     # check that neither of the matrices is empty
    #     if matrix.size == 0:
    #         raise TypeError(f'{names[idx]} can\'t be empty')
    #     # check that the matrices are of int type
    #     if matrix.dtype not in [int, float]:
    #         raise TypeError(f'{names[idx] must contain only ints or floats')
    # create the matrices
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    return m_a @ m_b


if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
