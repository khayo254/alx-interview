#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle
    for i in range(n):
        line = [1] * (i + 1)
        for j in range(1, i):
            line[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(line)
    return triangle
