#!/usr/bin/python3
""" Defines a function that retrns a list of lists of integers
representing the Pascal's triangle of n """


def pascal_triangle(n):
    """ returns a list of lists of ints rep-ing the pascal's triangle """
    triangle = []
    if n <= 0:
        return triangle
    elif n == 1:
        triangle.append([1])
        return triangle
    elif n == 2:
        return [[1], [1, 1]]
    else:
        # build the triangle
        curr = []
        prev = [1, 1]
        row = 3
        triangle = [[1], [1, 1]]
        while row <= n:
            col = 0
            # get the next row
            while col < row:
                if col == 0 or col == (row - 1):
                    curr.append(1)
                else:
                    curr.append(prev[col - 1] + prev[col])
                col += 1
            # append the row to the triangle
            triangle.append(curr)
            prev = curr
            curr = []  # reset to empty list
            row += 1
        return triangle
