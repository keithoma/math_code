""" The Rational class represents a rational number.
"""

import integer

class Rational():

    def __init__(self, numerator, denominator):
        """
        """
        if denominator == 0: raise ZeroDivisionError("Denominator cannot be zero!")
        try:
            self.sign        = -1 if numerator * denominator < 0 else 1
            self.numerator   = int(abs(numerator))
            self.denominator = int(abs(denominator))
        except TypeError:
            print("Type error. Construction of Rational object failed.")
        self.reduce()
    
    def reduce(self):
        d = integer.gcd(self.numerator, self.denominator)
        self.numerator   = self.numerator // d
        self.denominator = self.denominator // d
        return self

    def __str__(self):
        return "{}{} / {}".format("-" if self.sign < 0 else "", self.numerator, self.denominator)

    def __add__(self, right):
        return Rational(
            self.sign * self.numerator * right.denominator
            + right.sign * right.numerator * self.denominator,
            self.denominator * right.denominator
        )
    
    def __mul__(self, right):
        return Rational(
            self.sign * self.numerator * right.sign * right.numerator,
            self.denominator * right.denominator
        )

if __name__ == "__main__":
    frac1 = Rational(0, 3)
    frac2 = Rational(1, "a")
    print(frac1)
    print(frac2)
    print("\n\n")
    print(frac1 + frac2)
