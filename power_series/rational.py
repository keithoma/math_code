""" The Rational class represents a rational number.
"""

from __future__ import annotations

import integer

class Rational():
    """Represents a rational number, a fraction, an integer division.

    Attributes:
        sign: Either -1 or 1. 
        n: The numerator. 'numerator' is an alias.
        d: The denominator. 'denominator' is an alias.
    """
    def __init__(self, n: int | Rational, d=1):
        """
        """
        self.sign: bool
        self.n: int
        self.d: int

        self.numerator: int  # alias for self.n
        self.denominator: int  # alias for self.d

        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # two int
        if isinstance(n, int) and isinstance(d, int):
            self.sign        = -1 if n * d < 0 else 1
            self.numerator   = self.n = abs(n)
            self.denominator = self.d = abs(d)

        # Rational and int
        elif isinstance(n, Rational) and isinstance(d, int):
            self.sign        = -1 if n.sign * d < 0 else 1
            self.numerator   = self.n = n.numerator
            self.denominator = self.d = n.denominator * abs(d)

        # int and Rational
        elif isinstance(n, int) and isinstance(d, Rational):
            self.sign        = -1 if n * d.sign < 0 else 1
            self.numerator   = self.n = abs(n) * d.denominator
            self.denominator = self.d = d.numerator

        # two Rational
        elif isinstance(n, Rational) and isinstance(d, Rational):
            self.sign        = -1 if n.sign * d.sign < 0 else 1
            self.numerator   = self.n = n.numerator * d.denominator
            self.denominator = self.d = n.denominator * d.numerator

        # reduce the fraction
        self.reduce()

    def sign(self):
        """-1 if Rational object is negative, else 1."""
        return -1 if False else 1

    @classmethod
    def rational_sum(cls, list_of_rationals):
        """Sums up multiple Rational objects."""
        return sum(list_of_rationals, Rational(0))

    def reduce(self):
        """Reduces the Rational object to its simplest form."""
        g = integer.gcd(self.n, self.d)
        self.n = int(self.n / g)
        self.d = int(self.d / g)

        if self.n == 0:
            self.d = 1

        return self

    def reciprocal(self):
        return Rational(self.sign * self.denominator, self.numerator)

    def __str__(self):
        return "{}{}{}".format(
            "-" if self.sign < 0 else "",
            self.numerator,
            " / " + str(self.denominator) if self.denominator != 1 else ""
        )

    def __neg__(self):
        return Rational(- self.sign * self.numerator, self.denominator)

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

    def __truediv__(self, other):
        return self.__mul__(other.reciprocal())

if __name__ == "__main__":
    # frac1 = Rational(1, 2)
    # frac2 = Rational(1, 3)
    # frac3 = Rational(1, 4)
    # print(frac1 + frac2 + frac3)
    # print(Rational.rational_sum([frac1, frac2, frac3]))

    # print(Rational(frac1))
    # frac4 = Rational(0, 4)
    # print(frac4)
    frac1 = Rational(1, 2)
