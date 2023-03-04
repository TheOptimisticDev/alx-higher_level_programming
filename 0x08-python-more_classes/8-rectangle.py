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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare the areas of two `Rectangle` objects.
        Args:
            rect_1 (:obj:`Rectangle`): first rectangle
            rect_2 (:obj:`Rectangle`): second rectangle
        Returns:
            :obj:`Rectangle`: The rectangle with the larger area.
        Raises:
            TypeError: if `rect_1` or `rect_2` are not `Rectangle` instances.
        """

        if Rectangle is not type(rect_1):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if Rectangle is not type(rect_2):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        final_str = ''
        if self.__height == 0 or self.__width == 0:
            return final_str

        for i in range(self.__height):
            for j in range(self.__width):
                final_str += str(self.print_symbol)
            if j == self.__width - 1 and i == self.__height - 1:
                break

            final_str += '\n'

        return final_str

    def __repr__(self):

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        if type(self).number_of_instances > 0:
            type(self).number_of_instances -= 1
        print("Bye rectangle...")
