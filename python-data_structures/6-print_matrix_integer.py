#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ""
        for columns in row:
            line += "{:d} ".format(columns)
        line = line.rstrip()
        print(line)
