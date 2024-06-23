#!/usr/bin/env python
"""asdf"""

from __future__ import annotations

class Rational():
    """A rational number represented by a fraction.

    Attributes:
        _sign (int): -1 if negative, +1 if non-negative
        _numerator (int): Numerator. There are two getters for this value:
            'numerator' and simply 'n'.
        _denominator (int): Denominator. There are two getters for this value:
            'denominator' and simply 'd'.
    """

    def __init__(self, top: int | Rational, bot: int | Rational = 1):
        """Constructs a Rational object."""
        # handles the input and initalizes the attributes
        if isinstance(top, int):
            if isinstance(bot, int):
                self._sign        = -1 if top * bot < 0 else 1
                self._numerator   = abs(top)
                self._denominator = abs(bot)
            elif isinstance(bot, Rational):
                self._sign        = -1 if top * bot.sign < 0 else 1
                self._numerator   = abs(top) * bot.d
                self._denominator = bot.n
        elif isinstance(top, Rational):
            if isinstance(bot, int):
                self._sign        = -1 if top.sign * bot < 0 else 1
                self._numerator   = top.n
                self._denominator = top.d * abs(bot)
            elif isinstance(bot, Rational):
                self._sign        = -1 if top.sign * bot.sign < 0 else 1
                self._numerator   = top.n * bot.d
                self._denominator = top.d * bot.n
        else:
            raise TypeError("Invalid type for one or both arguments. "
                            "Expected int or Rational.")
        if self._denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # reduces the fraction to its simplest form
        self._reduce()

    ## Properties
    @property
    def sign(self) -> int:
        """Getter for the attribute '_sign'."""
        return self._sign

    @property
    def numerator(self) -> int:
        """Getter for the attribute '_numerator'."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Getter for the attribute '_denominator'."""
        return self._denominator

    @property
    def signed_numerator(self) -> int:
        """Returns the numerator with the appropriate sign."""
        return self._sign * self._numerator

    @property
    def signed_denominator(self) -> int:
        """Returns the denominator with the appropriate sign."""
        return self._sign * self._denominator

    @property
    def reciprocal(self) -> int:
        """Returns the reciprocal as Rational object."""
        return Rational(self.denominator, self.signed_numerator)

    # sometimes we want to use the shorter alias because they are more readable
    n = numerator
    d = denominator
    sgn_n = signed_numerator
    sgn_d = signed_denominator

    ## Magic Methods
    ### Comparisons
    def __eq__(self, other: Rational) -> bool:
        """Equal comparison."""
        return self.__dict__ == other.__dict__

    def __ne__(self, other: Rational) -> bool:
        """Not equal comparison."""
        return not self.__eq__(other)

    def __lt__(self, other: Rational) -> bool:
        """Less than comparison."""
        return self._compare(other) < 0

    def __le__(self, other: Rational) -> bool:
        """Less than or equal comparison."""
        return self._compare(other) <= 0

    def __gt__(self, other: Rational) -> bool:
        """Greater than comparison."""
        return self._compare(other) > 0

    def __ge__(self, other: Rational) -> bool:
        """Greater than or equal comparison."""
        return self._compare(other) >= 0

    ### Unary Operators and Functions
    def __pos__(self) -> Rational:
        """Returns the Rational number itself (positive sign)."""
        return self

    def __neg__(self) -> Rational:
        """Returns the negative of the Rational number."""
        return Rational(-self.signed_numerator, self.denominator)

    def __abs__(self) -> Rational:
        """Returns the absolute value of the Rational number."""
        return Rational(self.numerator, self.denominator)

    ### Arithmetic Operators
    def __add__(self, other: Rational) -> Rational:
        """Addition for two Rational objects."""        
        top = self.sgn_n * other.d + other.sgn_n * self.d
        bot = self.d * other.d
        return Rational(top, bot)

    def __sub__(self, other: Rational):
        return self + (-other)

    def __mul__(self, other: Rational) -> Rational:
        """Multiplication for two Rational objects."""
        top = self.sgn_n * other.sgn_n
        bot = self.d * other.d
        return Rational(top, bot)

    def __truediv__(self, other: Rational) -> Rational:
        """Division."""
        return self * other.reciprocal

    def __pow__(self, other: int) -> Rational:
        """Exponentiation of a Rational number to an integer power."""
        if other == 0:
            return Rational(1, 1)  # any number to the power of 0 is 1
        if other > 0:
            top = self.sgn_n ** other
            bot = self.d ** other
        else:
            top = self.d ** abs(other)
            bot = self.sgn_n ** abs(other)
        return Rational(top, bot)

    ### Reflected Arithmetic Operators
    def __radd__(self, other: Rational) -> Rational:
        """Reflected addition."""
        return self.__add__(other)

    def __rsub__(self, other: Rational) -> Rational:
        """Reflected subtraction."""
        return -self.__sub__(other)

    def __rmul__(self, other: Rational) -> Rational:
        """Reflected multiplication."""
        return self.__mul__(other)

    def __rtruediv__(self, other: Rational) -> Rational:
        """Reflected division."""
        return self.reciprocal.__mul__(other)

    ### Other
    def __str__(self) -> str:
        """Returns a printable String.
        
        Current format is: -1 / 3
        """
        pm = "-" if self.sign < 0 else ""
        right = " / " + str(self.d) if self.d != 1 else ""
        return f"{pm}{self.n}{right}"

    def __repr__(self) -> str:
        """Returns a string representation of the Rational object."""
        return f"Rational({self.sgn_n}, {self.d})"

    def __bool__(self) -> bool:
        """Returns True if the Rational number is not zero."""
        return self.n != 0

    ### Private Methods
    def _reduce(self) -> None:
        """Reduces the Rational object to its simplest form."""
        g = gcd(self._numerator, self._denominator)
        self._numerator   = self._numerator // g
        self._denominator = self._denominator // g

    def _compare(self, other: Rational) -> int:
        """Compares two Rational objects. Returns -1 if self < other, 0 if
        equal, 1 if self > other.
        """
        return (self - other > 0) - (self - other < 0)

def gcd(a: int, b: int) -> int:
    """Computes the gcd of two integers."""
    while b:
        a, b = b, a % b
    return abs(a)

def main() -> None:
    """Tests the class and methods implemented in this file."""
    R = Rational # a short hand we will use often
    print(R(3, 5))

if __name__ == "__main__":
    main()
