#!/usr/bin/python

"""
7th of October 2020

Class that represents a fractions or in general rational numbers.
"""

import copy
import math

class Rational():
    def __init__(self, numerator, denominator, sign=1):
        """
        Arguments:
            n (int) : numerator
            d (int) : denominator
            sign (int) : sign, 1 for positive and -1 for negative
        """
        # check here for valid arguments
        # TODO

        # save arguments as attributes
        self.sign         = sign
        self.numerator    = numerator
        self.denominator  = denominator

    # fraction handling
    def handle_sign(self):
        def get_sign(x): return (1, -1)[x < 0]
        self.sign         = self.sign * get_sign(self.numerator) * get_sign(self.denominator)
        self.numerator    = int(abs(self.numerator))
        self.denominator  = int(abs(self.denominator))
        return self

    def reduce_fraction(self):
        def gcd(n, m): return n if m == 0 else gcd(m, n % m)
        div = gcd(self.numerator, self.denominator)
        self.numerator   = int(self.numerator / div)
        self.denominator = int(self.denominator / div)
        return self

    def handle_float(self):
        pass

    def handle_all(self):
        self.handle_sign()
        self.reduce_fraction()
        self.handle_float()
        return self

    # printing methods
    def string_terminal(self): return "{s} {n} / {d}".format(s="-" if self.sign < 0 else "",
                                                             n=self.numerator, d=self.denominator)
    def string_latex(self): return "{s}\\frac{{{n}}}{{{d}}}".format(s="-" if self.sign < 0 else "",
                                                                    n=self.numerator, d=self.denominator)

    # magic methods
    """
    # care the unary magic methods do not create a copy
    def __pos__(self): return self
    def __neg__(self):
        self.sign = self.sign * -1
        return self
    def __abs__(self):
        self.sign = 1
        return self
    def __round__(self, n): return round(self.sign * self.numerator / self.denominator, n)
    def __floor__(self): return math.floor(self.sign * self.numerator / self.denominator)
    def __ceil__(self): return round(self.sign * self.numerator / self.denominator)
    def __trunc__(self): return round(self.sign * self.numerator / self.denominator)
    """

    def __str__(self):
        return self.string_terminal()

    def __add__(self, other):
        n = self.sign * self.numerator * other.denominator + other.sign * other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Rational(n, d).handle_all()

    def __sub__(self, other):
        n = self.sign * self.numerator * other.denominator - other.sign * other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Rational(n, d).handle_all()

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator,
                        sign=self.sign * other.sign)

    def __div__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator,
                sign=self.sign * other.sign)

def main():
    first = Rational(-3, 9, -1)
    second = Rational(12, 5)
    print(first)
    print(second)
    print(first - second)

if __name__ == "__main__":
    main()
