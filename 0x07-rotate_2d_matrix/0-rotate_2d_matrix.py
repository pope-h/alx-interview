#!/usr/bin/python3
""" Rotate 2D MatrixRotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    Function that rotates a 2D matrix by 90 degrees clockwise
    """
    reverse = matrix[::-1]
    matrix.clear()
    for index in range(len(reverse)):
        matrix.append([item[index] for item in reverse])
