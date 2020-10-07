#!/usr/bin/python

"""
7th of October 2020

Class that represents a fractions or in general rational numbers.
"""

class Rational():
    def __init__(self, numerator, denominator, sign=1):
        """
        Arguments:
            n (int) : numerator
            d (int) : denominator
            sign (int) : sign, 1 for positive and -1 for negative
        """
        # some auxilary one liners
        def get_sign(x): return (1, -1)[x < 0]
        def gcd(n, m): return n if m == 0 else gcd(m, n % m)
        div = gcd(numerator, denominator)

        # construct the rational number
        self.sign        = sign * get_sign(numerator) * get_sign(denominator)
        self.numerator   = int(abs(numerator) / div)
        self.denominator = int(abs(denominator) / div)

    def string_terminal(self): return "{} / {}".format(self.sign * self.numerator, self.denominator)
    def string_latex(self): return "{sign}\\frac{{{n}}}{{{d}}}".format(s="-" if self.sign < 0 else "",
                                                                       n=self.numerator, d=self.denominator)

def main():
    first = Rational(-3, 9, -1)
    print(first.string_latex())

if __name__ == "__main__":
    main()
