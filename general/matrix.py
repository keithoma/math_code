#!/usr/bin/env python
"""asdf"""

from __future__ import annotations

from rational import Rational as R

Number = int | R

class Matrix():
    """A (rational valued) m x n matrix.
    
    Attributes:
        _data (list[list[Number]]): The entries of the matrix as a list of
            list of Rational.
    """
    def __init__(self, raw: list[list[Number]]):
        """Constructs a matrix object."""
        # check 'raw' for type
        if not all(row and isinstance(row, list) for row in raw):
            raise TypeError("Input is not a list of list of Number.")

        # convert each cell from 'raw' to Rational and save
        self._data = [[R(cell) for cell in vector] for vector in raw]

        # verify the matrix is well-formed
        if len(set(len(row) for row in self._data)) > 1:
            raise ValueError("All rows must have the same number of columns.")

    ## Properties
    @property
    def shape(self) -> tuple[int]:
        """The shape of the matrix as a tuple of two ints. First value, m, is
        the number of rows, while the second value, n, is the number of
        columns.
        """
        return len(self._data), len(self._data[0])

    @property
    def is_square(self) -> bool:
        """True if the matrix square, false otherwiese."""
        m, n = self.shape
        return m == n

    ## Magic Methods
    ### Comparisons
    def __eq__(self, other: Matrix) -> bool:
        """Equal comparison."""
        return self.__dict__ == other.__dict__

    def __ne__(self, other: Matrix) -> bool:
        """Not equal comparison."""
        return not self.__eq__(other)

    ### Unary Operators and Functions
    def __pos__(self) -> Matrix:
        """Returns the Rational number itself (positive sign)."""
        return self

    def __neg__(self) -> Matrix:
        """Returns the negative of the Rational number."""
        return Matrix([[-cell for cell in vector] for vector in self._data])

    def __abs__(self) -> Matrix:
        """Returns the absolute value of the Rational number."""
        return Matrix(
            [[abs(cell) for cell in vector] for vector in self._data])

    ### Arithmetic Operators
    def __add__(self, other: Matrix) -> Matrix:
        """Addition for two Rational objects."""
        return Matrix(
            [[a + b for a, b in zip(v, w)]
             for v, w in zip(self._data, other._data)])

    def __sub__(self, other: Matrix):
        return self + (-other)

    def __mul__(self, other: Matrix) -> Matrix:
        """Multiplication for two Rational objects."""
        # TODO: implement this

    def __pow__(self, other: int) -> Matrix:
        """Exponentiation of a Rational number to an integer power."""
        # TODO: implement this

    ### Reflected Arithmetic Operators
    def __radd__(self, other: Matrix) -> Matrix:
        """Reflected addition."""
        return self.__add__(other)

    def __rsub__(self, other: Matrix) -> Matrix:
        """Reflected subtraction."""
        return -self.__sub__(other)

    def __rmul__(self, other: Matrix) -> Matrix:
        """Reflected multiplication."""
        # TODO: requires __mul__
        return self.__mul__(other)

    ### Other
    def __str__(self) -> str:
        """Returns a printable String.
        """
        # TODO: implement this
        return str(self._data)  # this is just a placeholder

    def __repr__(self) -> str:
        """Returns a string representation of the Rational object."""
        # TODO: implement this
        return str(self._data)  # this is just a placeholder

    ## Instance Methods
    def row(self, i: int) -> list[Number]:
        """Returns the i-th row."""
        # TODO:

    def column(self, j: int) -> list[Number]:
        """Returns the j-th column."""
        # TODO:

    def cell(self, i: int, j:int) -> Number:
        """Returns the entry at i-th row and j-th column."""
        return self._data[i - 1][j - 1]

    def scalar_multiplication(self, scalar: Number) -> Matrix:
        """Returns the product of the matrix and the scalar."""
        # TODO:

    def transpose(self) -> Matrix:
        """Returns the transpose."""
        # TODO:

def main() -> None:
    """Tests the class and methods implemented in this file."""
    # check for typing
    faulty_raws = [
        "a",               # not even a list
        [1, 2],            # not a list of list
        [[]],              # list of list, but empty
        [["a"]],           # list of list, but contains not a Number
        [[1, R(2), "a"]],  # same as above
        [[1, 2],
         [1]]              # mismatched rows
    ]


    for m in faulty_raws:
        try:
            Matrix(m)
            print(f"Incorrectly accepted \nm = {m}.")
        except (TypeError, ValueError) as error:
            print(f"Correctly rejected \nm = {m}.\nError: {error}")
            print()

    # check to Rational conversion
    m1 = Matrix(
        [[1, R(2)],
         [R(0), R(R(3, 5))]]
    )
    print(m1)

    m2 = Matrix(
        [[1, 0],
         [0, 0]]
    )
    print(m2)

    m3 = m1 + m2
    m4 = m1 - m2

    print(m3)
    print(m4)
    print("\n" + "-" * 80 + "\n\n")

    # check for cell
    print(m1)
    print(f"Shape: {m1.shape} | Is Square? = {m1.is_square}")
    print(m1.cell(1, 1))
    print(m1.cell(1, 2))
    print(m1.cell(2, 1))
    print(m1.cell(2, 2))

if __name__ == "__main__":
    main()
