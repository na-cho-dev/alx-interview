#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    result = [[None for _ in range(len(row))] for row in matrix]
    j = len(matrix) - 1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            result[col][j - row] = matrix[row][col]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = result[row][col]
