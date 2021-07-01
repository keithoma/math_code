#!/usr/bin/python

"""
1st of July 2021
"""

import numpy as np
import matplotlib.pyplot as plt

class LISetting():
    def __init__(self):
        self.show_data          = True
        self.show_polynomials   = False
        self.show_interpolation = True
        self.show_function      = True
        self.fineness           = 500

class LagrangeInterpolation():
    """
    data (2-dim list): 
    """
    def __init__(self, _data, _area, _n, _setting=LISetting()):

        def create_data(_the_function, _area, _n):
            """
            Creates a two-dimensional ndarray object from a function.

            Arguments:
                the_function (callable):
                area (tuple): (a, b)
                n (int):
            """
            h      = abs(_area[1] - _area[0]) / _n
            x_axis = [h * k for k in range(_n + 1)]
            y_axis = [_the_function(x) for x in x_axis]
            return np.array([x_axis, y_axis])

        if callable(_data):
            self.data = create_data(_data, _area, _n)
            self.the_function = _data
        elif isinstance(_data, np.ndarray):
            self.data = _data
        else:
            raise ValueError("Data parameter must be callable or two-dimensional ndarray object.")

        self.n = len(self.data[0])
        self.area = _area
        self.setting = _setting

    # computing
    def lagrange_polynomial(self, j, x):
        def X(i): return self.data[0][i]
        def Y(i): return self.data[1][i]
        return Y(j) * np.prod([(x - X(i)) / (X(j) - X(i)) for i in range(self.n) if j != i])

    def lagrange_interpolation(self):
        def Y(i): return self.data[1][i]
        return lambda x: sum([self.lagrange_polynomial(j, x) for j in range(self.n)])

    # plotting
    def plot_data(self):
        plt.plot(*self.data, 'bo')

    def plot_lagrange_polynomials(self):
        x_axis = np.linspace(*self.area, self.setting.fineness)
        for i in range(self.n):
            y_axis = [self.lagrange_polynomial(i, x) for x in x_axis]
            plt.plot(x_axis, y_axis)

    def plot_lagrange_interpolation(self):
        x_axis = np.linspace(*self.area, self.setting.fineness)
        y_axis = [self.lagrange_interpolation()(x) for x in x_axis]
        plt.plot(x_axis, y_axis)

    def plot_function(self):
        x_axis = np.linspace(*self.area, self.setting.fineness)
        y_axis = [self.the_function(x) for x in x_axis]
        plt.plot(x_axis, y_axis)

    def plot(self):
        if self.setting.show_data:
            self.plot_data()
        if self.setting.show_polynomials:
            self.plot_lagrange_polynomials()
        if self.setting.show_interpolation:
            self.plot_lagrange_interpolation()
        if self.setting.show_function and callable(self.the_function):
            self.plot_function()
        plt.show()

def main():

    data = np.array([
        [-3, 0, 3],
        [0.5, 2, -1]
    ])

    def a_function(x):
        return np.sin(x + np.cos(x))

    LI = LagrangeInterpolation(a_function, (0, 50), 10)
    LI.plot()

if __name__ == "__main__":
    main()
