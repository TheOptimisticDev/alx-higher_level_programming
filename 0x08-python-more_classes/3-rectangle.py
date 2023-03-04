#!/usr/bin/python3
"""Defines a `Rectangle` class."""


class Rectangle:
    """Definition of `Rectangle` class.
    Args:
        width (:obj:`int`, optional): width of `Rectangle` instance
        height (:obj:`int`, optional): height of `Rectangle` instance
    Attributes:
        width (int): width of `Rectangle` instance
        height (int): height of `Rectangle` instance
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Width of the rectangle
        Note:
            Setter raises a TypeError if `width` is not type `int`,
            and a ValueError if `width < 0`.
        """

        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """int: Height of the rectangle
        Note:
            Setter raises a TypeError if `value` is not type `int`,
            and a ValueError if `height < 0`.
        """

        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Return the area of a `Rectangle` instance.
        Returns:
            int: area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimater of a `Rectangle` instance.
        Returns:
            int: perimeter of rectangle, 0 if height == 0
                or width == 0.
        """
        if (self.__height == 0 or self.__width == 0):
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        str = ''
        if self.__height == 0 or self.__width == 0:
            return str

        for i in range(self.__height):
            for j in range(self.__width):
                str += '#'
            if j == self.__width - 1 and i == self.__height - 1:
                break

            str += '\n'

        return str
