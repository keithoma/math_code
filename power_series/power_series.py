""" Agenda:
* clean up

Notes:
* I might need to define two different kind of 'accuracies' ... when I multiply two polynomials,
I need self.acc + other.acc much precision, but the values themselves are only accurate up to
min(self.acc, other.acc)

Implements the PowerSeries class that represents a power series. A mathematical power series has
infinitely many coefficients, i.e. all polynomials may be viewed as a power series with almost all
coefficients being zero, but obviously we cannot save infinitely many coefficients. Thus, the
PowerSeries class defines an attribute called 'precision' that sets how many of the first
coefficients we will care about. The coefficients themselves are saved as a list of Rational
objects (see rational.py) in the attribute 'coefficients'.
"""
from __future__ import annotations
from rational import Rational as R

class PowerSeries():
    """Represents a (formal) power series.
    
    Attributes:
        coefficients: A list of Rational objects that represents the
          coefficients of a power series. The 0th entry is the constant term,
          the first entry is the monomial of first degree, and so on.
        coef: Alias of coefficients.
        precision: An integer that sets how many of the first coefficients we
          are going to look at. Negative values will be overwritten by the
          length of the 'coefficients'.
        prec: Alias of precision.
    """
    def __init__(self, coefficients: list[int], precision: int = -1):
        """Constructs a PowerSeries object.
        
        Args:
            coef: A list of ints.
            prec: An integer.
        """
        # We save the given coefficients as a list of Rational objects.
        # self.coef: list[R] = PowerSeries.to_rational(coef)
        self._coefficients: list[R] = coefficients

        # Save precision as an attribute. If the given value is negative, we
        # take the length of coefficients as our precision.
        if precision < 0:
            self._precision: int = len(self._coefficients) - 1
        else:
            self._precision: int = precision

        # Make sure that the PowerSeries matches the given precision in length.
        self.match_precision_to(self._precision)

    @property
    def coef(self) -> list[R]:
        return self._coefficients

    @coef.setter
    def coef(self, a) -> PowerSeries:
        self._coefficients = a
        return self

    @property
    def coefficients(self) -> list[R]:
        return self._coefficients

    @property
    def prec(self) -> int:
        return self._precision

    @prec.setter
    def prec(self, k: int) -> PowerSeries:
        self._precision = k
        return self

    @property
    def precision(self) -> int:
        return self._precision

    @precision.setter
    def precision(self, k: int) -> PowerSeries:
        self._precision = k
        return self

    @staticmethod
    def to_rational(coef: list[int]) -> list[R]:
        """Converts a list of int to list of Rational."""
        return [R(a) for a in coef]

    def match_precision_to(self, k: int = None) -> PowerSeries:
        """Appends zeros as Rational objects to 'coefficients' to match the
        'precision'.
        """
        # If a value was given for precision, update the attribute.
        if k is not None: self.prec(k)

        # Append 0s as Rational objects at the end of the coefficients
        self.coefficients(
            self.coef() + [R(0)] * (self.prec() + 1 - len(self.coef()))
        )

        return self

    def multiplicative_inverse(self) -> PowerSeries:
        """Computes the multiplicative inverse."""
        b = [R(1) / self.coef[0]] # b_0 = 1 / a_0

        # after b_0, the coefficients are computed recursivly
        # b_n = - (1 / a_0) * sum_{i=1}^n a_i b_{n-i}
        def next_coefficient(n: int) -> R:
            _ = -R(1) / self.coef[0]
            _ = _ * R.rational_sum(
                [self.coef[i] * b[n - i] for i in range(1, n + 1)])
            return _

        for k in range(1, self.prec):
            b.append(next_coefficient(k))

        return PowerSeries(b)

    def composition(self, other: PowerSeries) -> PowerSeries:
        pass

    def __str__(self) -> str:
        """Converts the list of coefficients as a readable string. Current
        format is (0, 1, 2).
        """
        output_string = "("
        for rational in self.coefficients:
            output_string += str(rational) + ", "
        output_string = output_string[:-2] + ")"
        return output_string

    def __pos__(self) -> PowerSeries:
        """Returns a copy of the object."""
        return PowerSeries(self.coef, self.prec)

    def __neg__(self) -> PowerSeries:
        """Returns a copy of the object, but the 'sign' is switched."""
        return PowerSeries([-x for x in self.coef], self.prec)

    def __add__(self, other) -> PowerSeries:
        self.prec = other.prec = max(self.prec, other.prec)
        self.match_precision_to()
        other.match_precision_to()
        return PowerSeries([l + r for l, r in zip(self.coef, other.coef)])

    def __radd__(self, other) -> PowerSeries:
        return self + other

    def __sub__(self, other) -> PowerSeries:
        return self - other

    def __rsub__(self, other) -> PowerSeries:
        return other - self

    def __mul__(self, other) -> PowerSeries:
        """Multiplies two PowerSeries.
        
        Product was implemented through Cauchy Product.

        https://en.wikipedia.org/wiki/Cauchy_product
        """
        # highest degree of the product is:
        self.prec = other.prec = self.prec + other.prec
        self.match_precision_to()
        other.match_precision_to()

        def c(k: int) -> R:
            _ = [self.coef[l] * other.coef[k - l] for l in range(k + 1)]
            return R.rational_sum(_)

        return PowerSeries([c(k) for k in range(self.precision + 1)])

    def __rmul__(self, other: PowerSeries):
        return self * other


    def __pow__(self, k: int):
        return [self for _ in range(k)]

def main() -> None:
    ps1 = PowerSeries([10, 7, 3, 1])
    print(ps1.__dict__)
    ps1.coef = [0]
    print(ps1.__dict__)
    return None


if __name__ == "__main__":
    main()
    # power1 = PowerSeries([1, 1, 1], 20)
    # power2 = PowerSeries([1, 0, -1, 2])
    # # print(power1.precision)
    # # print("------------")
    # # print(power1)
    # # print(power2)
    # # cauchy = power1.cauchy_product(power2)
    # # print(cauchy)
    # mul_inverse = power1.multiplicative_inverse()
    # print(power1)
    # print("\n\n\n")
    # print(mul_inverse)
    # print("\n\n\n")
    # print(power1 * mul_inverse)
    # # print(cauchy.precision)
