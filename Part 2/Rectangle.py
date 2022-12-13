class Rectangle:

    def __init__(self):
        self.__width = 1
        self.__length = 1

    def set_length(self, length):
        if 0.0 < length < 20.0:
            self.__length = length
        else:
            print("Incorrect number")

    def set_width(self, width):
        if 0.0 < width < 20.0:
            self.__width = width
        else:
            print("Incorrect number")

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def perimeter(self):
        print(self.__width + self.__width + self.__length + self.__length)

    def square(self):
        print(self.__width * self.__length)


pr = Rectangle()
pr.set_width(3.0)
pr.set_length(4.0)
pr.perimeter()
pr.square()
