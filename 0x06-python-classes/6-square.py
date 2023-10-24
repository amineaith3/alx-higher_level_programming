#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialisation of the square
        Args:
        size(int): the size of the square.
        position (int, int): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Set the current position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isintance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            print("")
