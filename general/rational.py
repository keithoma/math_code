"""The Rational class represents a rational number.
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
    # pylint: disable-next=useless-return
    def __init__(self, top: int | Rational, bot: int | Rational = 1) -> None:
        """Constructs a Rational object."""
        self._sign: int
        self._numerator: int
        self._denominator: int

        # handle the input and initalize the attributes
        self._initialize(top, bot)

        # reduce the fraction
        self._reduce()

        return None

    def _initialize(self, top: int | Rational, bot: int | Rational) -> None:
        """Initializes the attributes of the Rational object."""
        # bot cannot be zero
        if top == 0 and bot == 1:
            self._sign        = 1
            self._numerator   = 0
            self._denominator = 1
        elif bot == 0 or bot == Rational(0):
            raise ZeroDivisionError("Denominator cannot be zero.")

        if isinstance(top, int):
            if isinstance(bot, int):
                self._sign        = -1 if top * bot < 0 else 1
                self._numerator   = abs(top)
                self._denominator = abs(bot)
                return None
            if isinstance(bot, Rational):
                self._sign        = -1 if top * bot.sign < 0 else 1
                self._numerator   = abs(top) * bot.d
                self._denominator = bot.n
                return None

        if isinstance(top, Rational):
            if isinstance(bot, int):
                self._sign        = -1 if top.sign * bot < 0 else 1
                self._numerator   = top.n
                self._denominator = top.d * abs(bot)
                return None
            if isinstance(bot, Rational):
                self._sign        = -1 if top.sign * bot.sign < 0 else 1
                self._numerator   = top.n * bot.d
                self._denominator = top.d * bot.n
                return None

    def _reduce(self) -> None:
        """Reduces the Rational object to its simplest form."""
        if self._numerator == 0:
            self._denominator = 1
            return None

        g = integer.gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // g
        self._denominator = self._denominator // g

        return None

    @property
    def sign(self):
        """Getter for the attribute '_sign'."""
        return self._sign

    @property
    def numerator(self):
        """Getter for the attribute '_numerator'."""
        return self._numerator

    @property
    def signed_numerator(self):
        """Returns the numerator with the appropriate sign."""
        return self._sign * self._numerator

    @property
    def denominator(self):
        """Getter for the attribute '_denominator'."""
        return self._denominator

    @property
    def signed_denominator(self):
        """Returns the denominator with the appropriate sign."""
        return self._sign * self._denominator

    # sometimes we want to use the shorter alias because they are more readable
    n = numerator
    signed_n = signed_numerator
    d = denominator
    signed_d = signed_denominator

    @classmethod
    def rational_sum(cls, list_of_rationals: list[Rational]) -> Rational:
        """Sums up multiple Rational objects."""
        return sum(list_of_rationals, Rational(0))

    def reciprocal(self) -> Rational:
        """Returns the reciprocal of the object."""
        return Rational(self.signed_denominator, self.numerator)

    def __str__(self) -> str:
        """Returns a printable String.
        
        Current format is: -1 / 3
        """
        pm = "-" if self.sign < 0 else ""
        right = " / " + str(self.d) if self.d != 1 else ""
        return f"{pm}{self.n}{right}"

    def __repr__(self) -> str:
        """Returns a printable String.
        
        Current format is: -1 / 3, Equivalent to __str__().
        """
        pm = "-" if self.sign < 0 else ""
        right = " / " + str(self.denominator) if self.denominator != 1 else ""
        return f"{pm}{self.n}{right}"

    def __pos__(self) -> Rational:
        """Returns a copy of the object."""
        return Rational(self.signed_numerator, self.denominator)

    def __neg__(self) -> Rational:
        """Returns a copy of the object, but the 'sign' is switched."""
        return Rational(- self.signed_numerator, self.denominator)

    def __abs__(self) -> Rational:
        """Returns a copy of the object, but the sign is positive."""
        return Rational(self.numerator, self.denominator)

    def __add__(self, other: Rational) -> Rational:
        """Addition for two Rational objects."""
        n, d = self.sign * self.n, self.d
        p, q = other.sign * other.n, other.d
        return Rational(n * q + p * d, d * q)

    def __radd__(self, other: Rational) -> Rational:
        """Reverse addition for two Rational objects.
        
        Equivalent to __add__.
        """
        return self.__add__(other)

    def __sub__(self, other: Rational) -> Rational:
        """Subtraction of a Rational object from another."""
        return self - other

    def __rsub__(self, other: Rational) -> Rational:
        """Reversed subtraction of two Rational objects."""
        return other - self

    def __mul__(self, other: Rational) -> Rational:
        """Multiplication for two Rational objects."""
        n, d = self.sign * self.n, self.d
        p, q = other.sign * other.n, other.d
        return Rational(n * p, d * q)

    def __rmul__(self, other: Rational) -> Rational:
        """Reverse multiplication for two Rational objects.
        
        Equivalent to __mul__.
        """
        return self.__rmul__(other)

    def __truediv__(self, other: Rational) -> Rational:
        """Division for two Rational objects."""
        return self.__mul__(other.reciprocal())


def main():
    """Tests the class and methods implemented in this file."""
    # we will often use this shorthand
    R = Rational

    # here, we test the constructor
    frac1 = R(10, 20)
    print(f"R(10, 20) = {frac1}. (Should be '1 / 2'.)")

    frac2 = R(-6, 15)
    print(f"R(-6, 15) = {frac2}. (Should be '-2 / 5'.)")

    frac3 = R(frac1, 3)
    print(f"R((1/2) / 3) = {frac3}. (Should be '1 / 6'.)")

    frac4 = R(-7, frac2)
    print(f"R(-7 / (-2/5)) = {frac4}. (Should be '35 / 2'.)")

    frac5 = R(frac2, frac1)
    print(f"R((-2/5) / (1/2)) = {frac5}. (Should be '-4 / 5'.)")

    # test the property functions
    print(f"R(-2, 5).sign = {frac2.sign}")
    print(f"R(-2, 5).numerator = {frac2.numerator}")
    print(f"R(-2, 5).n = {frac2.n}")
    print(f"R(-2, 5).signed_numerator = {frac2.signed_numerator}")
    print(f"R(-2, 5).signed_n = {frac2.signed_n}")
    print(f"R(-2, 5).denominator = {frac2.denominator}")
    print(f"R(-2, 5).d = {frac2.d}")

if __name__ == "__main__":
    main()
