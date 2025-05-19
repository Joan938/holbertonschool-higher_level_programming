#!/usr/bin/python3
"""
Module for matrix multiplication.
Contains the function `matrix_mul` that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list of lists): First matrix containing integers or floats.
        m_b (list of lists): Second matrix containing integers or floats.

    Returns:
        list of lists: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, contains
        non-numeric data,
        or if rows are not of the same size.
        ValueError: If m_a or m_b is empty, or if they can't be multiplied.
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are empty
    if not m_a or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check if all elements in m_a and m_b are integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if all rows in m_a and m_b have the same size
    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = []
    for i in range(len(m_a)):  # Rows of m_a
        row = []
        for j in range(len(m_b[0])):  # Columns of m_b
            sum_product = 0
            for k in range(len(m_b)):  # Columns of m_a == Rows of m_b
                sum_product += m_a[i][k] * m_b[k][j]
            row.append(sum_product)
        result.append(row)

    return result
