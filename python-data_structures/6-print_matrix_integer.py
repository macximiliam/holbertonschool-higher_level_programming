#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for columns in row:
            print("{:d}".format(columns),end=" ")
        print()