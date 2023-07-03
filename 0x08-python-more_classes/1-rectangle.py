#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
    """"Instantiation with optional width and height"""
    self.width = width
    self.height = height

    @property
    def width(self):
        """ property width """
        return self.__width

    @property
    def height(self):
        """propertu height """
        return self.__height

    @width.setter
    def width(self, value):
        """ property set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """property set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
