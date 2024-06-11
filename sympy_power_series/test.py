"""Lagrange"""


import sympy as sp

from sympy import fps

X = sp.symbols('X')

class SPowerSeries():
    """"""
    def __init__(self, series):
        self.series = series

    def a(self): return self.series


    def u(self, k):
        _ = fps((1 / X) * self.series)
        _ = _.inverse(X, 6)
        print(_)
        _ = _ ** (k + 1)
        _ = _.expand()
        _ = _.coeff(X, k)
        print(_)

        return _
        
def main():

    sps = SPowerSeries(X + X ** 2)
    print(sps.series)
    for i in range(5):
        print(sps.u(i))

if __name__ == "__main__":
    main()