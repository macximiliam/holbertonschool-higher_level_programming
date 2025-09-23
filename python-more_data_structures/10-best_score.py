#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None

""" THIS IS OTHER SOLUCTION:
    def best_score(a_dictionary):
        def best_score(a_dictionary):
    if not a_dictionary:
        return None """