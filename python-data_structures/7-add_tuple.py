#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    a_fixed = []
    for i in range(2):
        if i < len(tuple_a):
            a_fixed.append(tuple_a[i])
        else:
            a_fixed.append(0)

    b_fixed = []
    for i in range(2):
        if i < len(tuple_b):
            b_fixed.append(tuple_b[i])
        else:
            b_fixed.append(0)
    result = (a_fixed[0] + b_fixed[0], a_fixed[1] + b_fixed[1])
    return result
