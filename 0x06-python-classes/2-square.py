#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Square"""
    def __init__(self, size=0):
        """Initialisation of the square 
        Args:
            size(int): the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
