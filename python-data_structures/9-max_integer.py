#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    bigger = my_list[0]

    for i in my_list[1:]:
        if i > bigger:
         bigger = i

    return bigger
