class Rectangle:

    def __init__(self):
        self.width = 1
        self.length = 1

    def set_length(self, length):
        if 0.0 < length < 20.0:
            self.length = length
        else:
            print("Incorrect number")

    def set_width(self, width):
        if 0.0 < width < 20.0:
            self.width = width
        else:
            print("Incorrect number")

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def perimeter(self):
        print(self.width + self.width + self.length + self.length)

    def square(self):
        print(self.width * self.length)


pr = Rectangle()
pr.set_width(3.0)
pr.set_length(4.0)
pr.perimeter()
pr.square()
