#!/usr/bin/python3
class Rectangle:
    """Class that defines a rectangle."""


    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width


