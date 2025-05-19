#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The function `matrix_divided` takes a matrix (list of lists) of integers or
floats and divides each element by a given divisor, returning a new matrix
with rounded results.

Requirements:
- The matrix must be a list of lists containing integers or floats.
- Each row in the matrix must have the same size.
- The divisor must be a number (integer or float) and cannot be zero.

Raises:
- TypeError: If the matrix is not a list of lists of integers/floats.
- TypeError: If each row of the matrix is not of the same size.
- TypeError: If the divisor is not a number.
- ZeroDivisionError: If the divisor is zero.

Example usage:
>>> matrix_divided([[4, 8], [16, 32]], 2)
[[2.0, 4.0], [8.0, 16.0]]

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor.

    Returns:
    list of lists of float: A new matrix with elements divided by div,
    rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
    TypeError: If each row of the matrix is not of the same size.
    TypeError: If div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0]) if matrix else 0
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
