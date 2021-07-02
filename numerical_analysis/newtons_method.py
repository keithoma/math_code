#!/usr/bin/python

"""
2nd of July 2021

the rest is matter of scaling and finding the notes
"""

import numpy as np
import matplotlib.pylab as plt


class NewtonsMethod:
    def __init__(self, _the_fun, _the_der, _area,  _start, _n):
        self.the_fun = _the_fun
        self.the_der = _the_der
        self.area    = _area
        self.start   = _start
        self.n       = _n

    def next(self, _x0) -> float:
        return _x0 - (self.the_fun(_x0) / self.the_der(_x0))

    def iterate(self, _start, _n) -> np.ndarray:
        arr = [_start]
        for i in range(_n):
            arr.append(self.next(arr[-1]))
        return np.array(arr)
    
    def plot_function(self):
        x_axis = np.linspace(*self.area, 500)
        y_axis = [self.the_fun(x) for x in x_axis]
        plt.plot(x_axis, y_axis)
        return self

    def plot_iterations(self):
        x_axis = self.iterate(self.start, self.n)
        y_axis = [self.the_fun(x) for x in x_axis]
        plt.plot(x_axis, y_axis, 'bo')
        print(x_axis)
        return self

    def plot(self):
        self.plot_iterations()
        self.plot_function()
        plt.show()
        return self

def main():
    def a_function(x): return 10 * np.sin((1 / 10) * (x + np.sin(x)) - 5)
    def a_derivative(x): return (1 + np.cos(x)) * np.cos(5 - (x / 10) - (np.sin(x) / 10))
    NM = NewtonsMethod(a_function, a_derivative, (-100, 100), 0, 30)
    NM.plot()

if __name__ == "__main__":
    main()
