#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    # Initation methods

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if type(Rectangle.print_symbol) == list:
            print(Rectangle.print_symbol[1])
        returnStr = ""

        if self.__width == 0 or self.__height == 0:
            returnStr = ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    if j == self.__width - 1 and i != self.__height - 1:
                        returnStr += str(self.print_symbol) + "\n"
                    elif j == self.__width - 1 and i == self.__height - 1:
                        returnStr += str(self.print_symbol)
                    else:
                        returnStr += str(self.print_symbol)

        return returnStr

    def __repr__(self):
        return 'Rectangle(' + str(self.__width) + ','+ str(self.__height) + ')'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Static Methods

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    #Setters and Getters

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    #Public Methods

    def area(self):
        areaResult = self.__width * self.__height
        return areaResult

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter
