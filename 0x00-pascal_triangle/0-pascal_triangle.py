#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers representing the
Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    else list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascalArray = []
    for row in range(n):
        colArray = [None] * (row + 1)
        colArray[0], colArray[-1] = 1, 1
        for col in range(1, row):
            colArray[col] = (
                pascalArray[row - 1][col - 1] + pascalArray[row - 1][col])

        pascalArray.append(colArray)

    return pascalArray
