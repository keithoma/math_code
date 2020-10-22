#!/usr/bin/python

"""
22th of October 2020
"""

import numpy as np
import matplotlib.pyplot as plt

class LagrangeInterpolation():
    def __init__(self, data):
        self.data = data
        self.n = len(data[0])
    
    def X(self, i):
        return self.data[0][i]

    def lagrange_polynomial(self, i, x):
        return self.data[1][i] * np.prod([(x - self.X(j)) / (self.X(i) - self.X(j)) for j in range(self.n) if j != i])

    def plot_data(self):
        plt.plot(*self.data, 'bo')

    def plot_lagrange_polynomials(self):
        x_axis = np.linspace(-3, 3, 500)
        for i in range(self.n):
            y_axis = [self.lagrange_polynomial(i, x) for x in x_axis]
            plt.plot(x_axis, y_axis)

def main():
    data = [
        [-3, 0, 3],
        [0.5, 2, -1]
    ]
    LI = LagrangeInterpolation(data)
    LI.plot_data()
    LI.plot_lagrange_polynomials()
    plt.show()

if __name__ == "__main__":
    main()


