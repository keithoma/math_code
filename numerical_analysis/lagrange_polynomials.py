#!/usr/bin/python

"""
1st of July 2021

Class that formats given input into WolframAlpha-interpretable Lagrange polynomials.
"""

class LagrangePolynomial():
    def __init__(self, _data, _a, _b, _n):

        def create_data(_the_function, _a, _b, _n):
            self.xdata = ["({k} abs({a} - {b}) / {n})".format(k=k, a=_a, b=_b, n=_n) for k in range(_n + 1)]
            self.ydata = [_the_function(x) for x in self.xdata]
        # self.xdata = _xdata
        # self.ydata = _ydata

        create_data(_data, _a, _b, _n)

    def lagrange_polynomial(self, j) -> str:
        def X(i): return str(self.xdata[i])
        def Y(i): return str(self.ydata[i])
        pol = str(self.ydata[j])
        for i in range(len(self.xdata)):
            if i != j:
                pol += " * ((x - {0}) / ({1} - {0}))".format(X(i), X(j))
        return pol

def main():
    def a_function(_x) -> str:
        return "sin({0}) * {0}".format(_x)

    LP = LagrangePolynomial(a_function, 0, 4, 4)
    print(LP.lagrange_polynomial(1))


 * ((x - (3 abs(0 - 4) / 4)) / ((1 abs(0 - 4) / 4) - (3 abs(0 - 4) / 4))) * ((x - (4 abs(0 - 4) / 4)) / ((1 abs(0 - 4) / 4) - (4 abs(0 - 4) / 4)))


if __name__ == "__main__":
    main()
