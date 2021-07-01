#!/usr/bin/python

"""
1st of July 2021
"""

from library_dystopia.rationalnumber import RationalNumber as RN
from library_dystopia.algebraicnumber import AlgebraicNumber as AN

class LagrangePolynomial():
    def __init__(self, _xdata, _ydata):
        self.xdata = _xdata
        self.ydata = _ydata

    def lagrange_polynomial(self, j, x):
        def X(i): return str(self.xdata[i])
        def Y(i): return str(self.ydata[i])
        pol = str(self.ydata[j])
        for i in range(len(self.xdata)):
            pol += "\\frac{x - {0}}{{1} - {0}} \\cdot".format(X(i), X(j))
        return self

def main():
    xdata = [0, 1, 2]
    ydata = [RN(-1, 2), "sin(pi)", 3]
    LP = LagrangePolynomial(xdata, ydata)
    



alg = AN([RN(1, 2), RN(3, 2)], ["pi", "sin(3)"])

print(alg.string_latex())