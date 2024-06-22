"""The Rational class represents a rational number.
"""

from __future__ import annotations
from integer import _int_gcd as gcd

class Rational():
    """Represents a rational number, a fraction, an integer division.

    Attributes:
        _sign (bool): -1 if negative, +1 if positive or zero
        _numerator (int): The numerator. 'numerator' is an alias.
        _denominator (int): The denominator. 'denominator' is an alias.
    """
    def __init__(self, top: int | Rational, bot: int | Rational = 1):
        """Constructs a Rational object."""
        # handle the input and initalize the attributes
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

        # check for dividing by zero
        if self._denominator == 0:
            raise ZeroDivisionError()

        # reduce the fraction
        g = gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // g
        self._denominator = self._denominator // g

    @property
    def sign(self) -> int:
        """Getter for the attribute '_sign'."""
        return self._sign

    @property
    def numerator(self) -> int:
        """Getter for the attribute '_numerator'."""
        return self._numerator

    @property
    def signed_numerator(self) -> int:
        """Returns the numerator with the appropriate sign."""
        return self._sign * self._numerator

    @property
    def denominator(self) -> int:
        """Getter for the attribute '_denominator'."""
        return self._denominator

    @property
    def signed_denominator(self) -> int:
        """Returns the denominator with the appropriate sign."""
        return self._sign * self._denominator

    @property
    def reciprocal(self) -> int:
        """."""
        return Rational(self.denominator, self.signed_numerator)

    # sometimes we want to use the shorter alias because they are more readable
    n = numerator
    sgn_n = signed_numerator
    d = denominator
    sgn_d = signed_denominator

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

    def __pos__(self) -> Rational:
        pass

    def __neg__(self) -> Rational:
        pass

    def __abs__(self) -> Rational:
        pass

    def __add__(self, other: Rational) -> Rational:
        """Addition for two Rational objects."""        
        top = self.sgn_n * other.d + other.sgn_n * self.d
        bot = self.d * other.d
        return Rational(top, bot)

    def __sub__(self, other: Rational):
        pass

    def __mul__(self, other: Rational) -> Rational:
        """Multiplication for two Rational objects."""
        top = self.sgn_n * other.sgn_n
        bot = self.d * other.d
        return Rational(top, bot)

    def __truediv__(self, other: Rational) -> Rational:
        """Division."""
        return self * other.reciprocal

    def __pow__(self, other: int) -> Rational:
        pass

    def __radd__(self, other: Rational) -> Rational:
        pass

    def __rsub__(self, other: Rational) -> Rational:
        pass

    def __rmul__(self, other: Rational) -> Rational:
        pass

    def __rtruediv__(self, other: Rational) -> Rational:
        pass

    def __iadd__(self, other: Rational) -> Rational:
        pass

    def __isub__(self, other: Rational) -> Rational:
        pass

    def __imul__(self, other: Rational) -> Rational:
        pass

    def __itruediv__(self, other: Rational) -> Rational:
        pass

    def __str__(self) -> str:
        """Returns a printable String.
        
        Current format is: -1 / 3
        """
        pm = "-" if self.sign < 0 else ""
        right = " / " + str(self.d) if self.d != 1 else ""
        return f"{pm}{self.n}{right}"

    def __nonzero__(self) -> bool:
        pass

    def _compare(self, other: Rational) -> int:
        """Compares two Rational objects. Returns -1 if self < other, 0 if
        equal, 1 if self > other.
        """
        diff = self.sgn_n * other.d - other.sgn_n * self.d
        return (diff > 0) - (diff < 0)

def main():
    """Tests the class and methods implemented in this file."""
    print(R(3, 5))

if __name__ == "__main__":
    main()
