#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print(f"{k}: {a_dictionary[k]}") for k in sorted(a_dictionary)]
""" this is other soluction: for k in sorted(a_dictionary):
                                print(f"{k}: {a_dictionary[k]}") """
