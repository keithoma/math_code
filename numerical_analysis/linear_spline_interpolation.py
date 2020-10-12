#!/usr/bin/python

"""
7th of October 2020
"""

import matplotlib.pyplot as plt
import numpy as np

DEFAULT_SETTINGS = {
    "range": [-1, 1],
    "fineness": 100, # the fineness of each spline; not to be confused with the number nodes
    "print-mode": "latex"
}

class LinearSplineInterpolation:
    def __init__(self, f, n, stg=DEFAULT_SETTINGS):
        """
        data_points should be a list of lists containing exactly two elements

        Arguments:
            f (callable) : the exact function to be interpolated
            n (int) : the number of splines, the number of grid points would be (n + 1)
        """
        self.f = f
        self.n = n
        self.stg = stg

        self.data_points = [[x, f(x)] for x in np.linspace(*stg["range"], n + 1)]

    def data_exact(self):
        grid = np.linspace(*self.stg["range"], self.stg["fineness"] * self.n)
        return grid, [self.f(x) for x in grid]

    def data_polynomial(self, start, end):
        """
        start and end should be a list containing exactly two elements
        """
        def s(x): return (start[1] * (end[0] - x) + end[1] * (x - start[0])) / (end[0] - start[0])
        local_grid = np.linspace(start[0], end[0], self.stg["fineness"])
        return local_grid, [s(x) for x in local_grid]

    def data_spline(self):
        """
        pieces together the linear functions constructed above
        """
        global_grid = []
        spline = []
        for i in range(self.n):
            local_grid, s = self.data_polynomial(self.data_points[i], self.data_points[i + 1])
            global_grid.extend(local_grid)
            spline.extend(s)
        return global_grid, spline

    def string_polynomial(self, start, end):
        sum1 = "{} * {}".format(start[1], end[0] + " - x")
        sum2 = "{} * {}".format(end[1], ("x - " + start[0]))
        return "\\frac{{}}{{}}".format(sum1 + sum2, end[0] - start[0])

"""
    def string_spline(self):
        string = ""
        for i in range(n):
"""

def main():
    """
    DEMONSTRATION.
    """
    # make this shorter
    def debug(f, n, stg=DEFAULT_SETTINGS):
        LSI = LinearSplineInterpolation(f, n, stg)
        print("n                     = {}".format(LSI.n))
        print("number of data points = {}".format(len(LSI.data_points)))

    def demonstration(f, n, setting={"range": [-1, 1], "fineness": 500}):
        LSI = LinearSplineInterpolation(f, n)

        plt.plot(*LSI.data_spline())
        plt.title("Number of nodes: {}".format(n))
        plt.show()

    debug(lambda x: 1 + 3 * x ** 3 + 5 * x ** 5, 4)

    demonstration(lambda x: 1 + 3 * x ** 3 + 5 * x ** 5, 4)


    # demonstration with x * sin(x)
    wider_range = {"range": [-10, 10], "fineness": 500}
    demonstration(lambda x: x * np.sin(x), 10, setting=wider_range)
    demonstration(lambda x: x * np.sin(x), 20, setting=wider_range)

    # demonstration with the Runge function
    def runge_function(x):
        return 1 / (1 + 25 * (x ** 2))

    for n in range(2, 22, 2):
        demonstration(runge_function, n)

    for n in range(3, 23, 2):
        demonstration(runge_function, n)

    for n in range(3, 23, 2):
        demonstration(runge_function, n, setting=wider_range)

if __name__ == "__main__":
    main()
