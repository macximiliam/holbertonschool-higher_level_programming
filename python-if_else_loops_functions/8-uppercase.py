#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
