#!/usr/bin/python3
"""Defines the add(a, b) function"""


def add_integer(a, b=98):
    """Returns the addition of int(a) and int(b)

    Raises:
    TypeError if a or b are not integers
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
