#!/usr/bin/python3
import sys
if __name__ == "__main__":

    arguments = sys.argv[1:]

    num_args = len(arguments)

    if num_args == 1:
        print(f"1 argumen : ")
    else:
        print(f"{num_args} arguments : ")

    if num_args > 0:
        for i, arg in enumerate(arguments, 1):
            print(f"{i}: {arg}")
