#!/usr/bin/python3
"""Writing a function for Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a lists of integers
    representing the Pascal’s triangle
        
    Parameters:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.

    """
    triangle = []

    if n <= 0:
        return []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                row.append(1)
            else:
                row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
        triangle.append(row)
    return triangle
