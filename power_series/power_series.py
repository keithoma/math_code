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
    def __init__(self, list_of_int: list[int], k: int = -1):
        """Constructs a PowerSeries object.
        
        Args:
            coef: A list of ints.
            prec: An integer.
        """
        # We save the given coefficients as a list of Rational objects.
        self._coefficients: list[R] = self.to_rational(list_of_int)

        # Save precision as an attribute. If the given value is negative, we
        # take the length of coefficients as our precision.
        if k < 0:
            self._precision: int = len(self._coefficients) - 1
        else:
            self._precision: int = k

        # Make sure that the PowerSeries matches the given precision in length.
        self.match_precision_to(self._precision)

    @staticmethod
    def to_rational(list_of_int: list[int]) -> list[R]:
        """Converts a list of int to list of Rational."""
        return [R(a) for a in list_of_int]

    def match_precision_to(self, k: int = None) -> None:
        """Appends zeros as Rational objects to 'coefficients' to match the
        'precision'.
        """
        # If a value was given for precision, update the attribute.
        if k is not None:
            self._precision = k

        # Append 0s as Rational objects at the end of the coefficients
        self._coefficients += [R(0)] * (
            self._precision + 1 - len(self._coefficients)
        )

    @property
    def coefficients(self) -> list[R]:
        """Coefficients of the power series."""
        return self._coefficients

    @coefficients.setter
    def coefficients(self, a) -> None:
        self._coefficients = a

    @property
    def precision(self) -> int:
        """Precision, i.e. the number of the first coefficients we care about."""
        return self._precision

    @precision.setter
    def prec(self, k: int) -> None:
        self._precision = k

    # alias for coef and prec
    coef = coefficients
    prec = precision

    def __str__(self) -> str:
        """Converts the list of coefficients as a readable string. Current
        format is (0, 1, 2).
        """
        output_string: str = "("
        for number in self.coef:
            output_string += str(number) + ", "
        output_string = output_string[:-2] + ")"
        return output_string

    def __pos__(self) -> PowerSeries:
        """Returns a copy of the object."""
        return PowerSeries(self.coef, self.prec)

    def __neg__(self) -> PowerSeries:
        """Returns a copy of the object, but the 'sign' is switched."""
        return PowerSeries([-x for x in self.coef], self.prec)

    def __add__(self, other) -> PowerSeries:
        """Adds two power series together."""
        self.prec = other.prec = max(self.prec, other.prec)
        self.match_precision_to()
        other.match_precision_to()
        return PowerSeries([l + r for l, r in zip(self.coef, other.coef)])

    def __radd__(self, other) -> PowerSeries:
        """Reverse addition."""
        return self + other

    def __sub__(self, other) -> PowerSeries:
        """Subtraction of two power series."""
        return self - other

    def __rsub__(self, other) -> PowerSeries:
        """Reverse subtraction."""
        return other - self

    def __mul__(self, other) -> PowerSeries:
        """Multiplies two PowerSeries.
        
        Product was implemented through Cauchy Product.

        https://en.wikipedia.org/wiki/Cauchy_product
        """
        # highest degree of the product is:
        h = self.prec + other.prec
        self.match_precision_to(h)
        other.match_precision_to(h)

        def c(k: int) -> R:
            _ = [self.coef[l] * other.coef[k - l] for l in range(k + 1)]
            return R.rational_sum(_)

        return PowerSeries([c(k) for k in range(self.prec + 1)])

    def __rmul__(self, other: PowerSeries) -> PowerSeries:
        return self * other

    def __pow__(self, k: int) -> PowerSeries:
        """Raises the power series to the integer power k."""
        if k < 0:
            raise ValueError("Negative powers are not supported for PowerSeries.")
        if k == 0:
            return PowerSeries([1], self.prec)  # P(x)^0 = 1

        result = PowerSeries([1], self.prec)
        base = self

        for _ in range(k):
            result = result * base

        return result

    def multiplicative_inverse(self) -> PowerSeries:
        """Computes the multiplicative inverse."""
        # b_0 = 1 / a_0
        b = [R(1) / self.coef[0]]

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
        """Computes the composition, i.e. self(other(X))."""
        _ = self.prec * other.prec
        self.match_precision_to(_)
        other.match_precision_to(_)

        result_coefs = [R(0)] * (self.prec + 1)
        other_power = PowerSeries([1], self.prec)  # Start with the series representing 1

        for number in self.coef:
            term = PowerSeries([number], self.prec) * other_power
            for j in enumerate(term.coef):
                if j[0] < len(result_coefs):
                    result_coefs[j[0]] += term.coef[j[0]]
            other_power = other_power * other

        return PowerSeries(result_coefs, self.prec)

    def lagrange_inversion_formula(self) -> PowerSeries:
        """Compute the Lagrange inversion formula to find the inverse of the power series."""
        #  if self.coef[0] != R(0):
        #      raise ValueError("The constant term must be zero for the Lagrange inversion formula.")

        # We need the multiplicative inverse of the derivative of the series.
        derivative_series = self.derivative()

        # Compute the coefficients for the inverse series using the formula.
        inverse_coeffs = [R(0)]  # Since the constant term for the inverse will be zero.
        for n in range(1, self.prec + 1):
            term_sum = R(0)
            for k in range(n):
                term_sum += (R(k + 1) * derivative_series.coef[k]) * inverse_coeffs[n - k - 1]
            inverse_coeff = -term_sum / derivative_series.coef[0]
            inverse_coeffs.append(inverse_coeff)

            print(inverse_coeff)

        return PowerSeries(inverse_coeffs)

    def derivative(self) -> PowerSeries:
        """Compute the derivative of the power series."""
        if len(self.coef) <= 1:
            return PowerSeries([0])  # Derivative of a constant term is zero.

        derivative_coeffs = [R(i) * self.coef[i] for i in range(1, len(self.coef))]
        return PowerSeries(derivative_coeffs)

# Example to test the lagrange_inversion_formula method:
def main() -> None:
    ps1 = PowerSeries([0, 1, 2, 3, 4], 10)
    inv = ps1.lagrange_inversion_formula()
    print(ps1)
    print(inv)
    # inverse_ps1 = ps1.lagrange_inversion_formula()
    # print(f"Original Power Series: {ps1}")
    # print(f"Inverse Power Series: {inverse_ps1}")
    # print(f"Product {ps1.composition(inverse_ps1)}")

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
