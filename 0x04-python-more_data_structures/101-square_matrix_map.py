#!/usr/bin/python3
# Function squares all integers in a matrix #
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
