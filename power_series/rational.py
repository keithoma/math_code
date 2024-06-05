""" The Rational class represents a rational number.
"""

import integer

class Rational():

    def __init__(self, numerator, denominator=1):
        """
        """
        # check if the arguments are integers
        # I don't want to do it the Pythonian way, I need to make sure that we are working with
        # integers
        if not isinstance(numerator, int): raise TypeError("Numerator must be an integer.")
        if not isinstance(denominator, int): raise TypeError("Denominator must be an integer.")

        if denominator == 0: raise ZeroDivisionError("Denominator cannot be zero.")

        # save the attributes
        self.sign        = -1 if numerator * denominator < 0 else 1
        self.numerator   = int(abs(numerator))
        self.denominator = int(abs(denominator))

        # reduce the fraction
        self.reduce()
    
    def reduce(self):
        d = integer.gcd(self.numerator, self.denominator)
        self.numerator   = self.numerator // d
        self.denominator = self.denominator // d
        return self

    def __str__(self):
        return "{}{}{}".format(
            "-" if self.sign < 0 else "",
            self.numerator,
            " / " + str(self.denominator) if self.denominator != 1 else ""
        )

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
    frac1 = Rational(1, 3)
    frac2 = Rational(1, 1)
    print(frac1)
    print("{}.....".format(frac2))
    print("\n\n")
    print(frac1 + frac2)
