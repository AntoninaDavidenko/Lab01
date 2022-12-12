class Rational:

    def __init__(self):
        self.numerator = 1
        self.denominator = 2

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def standard_form(self):
        print(f"{self.numerator}/{self.denominator}")

    def floating_point(self):
        result = self.numerator / self.denominator
        print(result)


pr = Rational()
pr.set_numerator(3)
pr.set_denominator(4)
pr.standard_form()
pr.floating_point()
