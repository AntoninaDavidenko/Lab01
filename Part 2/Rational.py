class Rational:

    def __init__(self):
        self.__numerator = 1
        self.__denominator = 2

    def set_numerator(self, numerator):
        self.__numerator = numerator

    def set_denominator(self, denominator):
        self.__denominator = denominator

    def standard_form(self):
        print(f"{self.__numerator}/{self.__denominator}")

    def floating_point(self):
        result = self.__numerator / self.__denominator
        print(result)


pr = Rational()
pr.set_numerator(3)
pr.set_denominator(4)
pr.standard_form()
pr.floating_point()
