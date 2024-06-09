""" The Rational class represents a rational number.
"""

import integer

class Rational():

    def __init__(self, number, denominator=1):
        """
        """
        # clearly, this is the most important thing to check
        if denominator == 0: raise ZeroDivisionError("Denominator cannot be zero.")

        # if the given number is already a rational number and the denominator is 1, we can just
        # save the values of the given rational number as attributes
        if isinstance(number, int) and isinstance(denominator, int):
            self.sign        = -1 if number * denominator < 0 else 1
            self.numerator   = abs(number)
            self.denominator = abs(denominator)
            return
        elif isinstance(number, Rational) and isinstance(denominator, int):
            self.sign        = -1 if number.sign * denominator < 0 else 1
            self.numerator   = number.numerator
            self.denominator = number.denominator * abs(denominator)
            return
        elif isinstance(number, int) and isinstance(denominator, Rational):
            self.sign        = -1 if number * denominator.sign < 0 else 1
            self.numerator   = number * denominator.denominator
            self.denominator = denominator.numerator
            return
        elif isinstance(number, Rational) and isinstance(denominator, Rational):
            self.sign        = -1 if number.sign * denominator.sign < 0 else 1
            self.numerator   = number.numerator * denominator.denominator
            self.denominator = number.denominator * denominator.numerator
            return

        # reduce the fraction
        self.reduce()

    @classmethod
    def rational_sum(cls, list_of_rationals):
        # apparantly, I have to pass a neutral element for the sum to work with magic methods
        # also note that the sum() function uses __radd__
        return sum(list_of_rationals, Rational(0))

    def reduce(self):
        d = integer.gcd(self.numerator, self.denominator)
        self.numerator   = self.numerator // d
        self.denominator = self.denominator // d
        return self

    def reciprocal(self):
        return Rational(self.sign * self.denominator, self.numerator)

    def __str__(self):
        return "{}{}{}".format(
            "-" if self.sign < 0 else "",
            self.numerator,
            " / " + str(self.denominator) if self.denominator != 1 else ""
        )

    def __add__(self, other):
        """ Addition for two Rational object.
        """
        return Rational(
            self.sign * self.numerator * other.denominator
            + other.sign * other.numerator * self.denominator,
            self.denominator * other.denominator
        )
    
    def __radd__(self, other):
        """ Reverse addition for two Rational object. Equivalent to __add__.
        """
        return self.__add__(other)

    def __mul__(self, other):
        return Rational(
            self.sign * self.numerator * other.sign * other.numerator,
            self.denominator * other.denominator
        )

    def __rmul__(self, other):
        return self.__rmul__(other)

if __name__ == "__main__":
    frac1 = Rational(1, 2)
    frac2 = Rational(1, 3)
    frac3 = Rational(1, 4)
    print(frac1 + frac2 + frac3)
    print(Rational.rational_sum([frac1, frac2, frac3]))

    print(Rational(frac1))