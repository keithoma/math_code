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
        if isinstance(number, Rational):
            self.sign        = number.sign
            self.numerator   = number.numerator
            self.denominator = number.denominator
            return

        # check if the arguments are integers
        # I don't want to do it the Pythonian way, I need to make sure that we are working with
        # integers
        if not isinstance(number, int): raise TypeError("Numerator must be an integer.")
        if not isinstance(denominator, int): raise TypeError("Denominator must be an integer.")


        # save the attributes
        self.sign        = -1 if number * denominator < 0 else 1
        self.numerator   = int(abs(number))
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
    
    def __radd__(self, other):
        return self.__add__(other)
    
    @classmethod
    def rational_sum(cls, list_of_rationals):
        # apparantly, I have to pass a neutral element for the sum to work with magic methods
        # also note that the sum() function uses __radd__
        return sum(list_of_rationals, Rational(0))

    def __mul__(self, right):
        return Rational(
            self.sign * self.numerator * right.sign * right.numerator,
            self.denominator * right.denominator
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