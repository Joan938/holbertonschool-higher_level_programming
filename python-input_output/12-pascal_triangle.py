#!/usr/bin/python3
""" 12-main """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) < n:
        new_row = [1]
        for i in range(1, len(triangle[-1])):
            new_row.append(triangle[-1][i - 1] + triangle[-1][i])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
