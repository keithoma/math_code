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

    def plot_splines(self):

        plt.plot(*self.data_exact())
        plt.plot(*self.data_spline())

        # auxilary lines to indicate the nodes
        for xi in np.linspace(*self.stg["range"], self.n + 1):
            plt.axvline(xi, linestyle=":", color="black")

        plt.title("Number of splines (n): {}\n(Number of nodes: {})".format(self.n, self.n + 1))
        plt.show()

    def string_polynomial(self, start, end):
        sum1 = "{} * ({})".format(start[1], str(end[0]) + " - x")
        sum2 = "{} * ({})".format(end[1], ("x - " + str(start[0])))
        return "\\frac{{{}}}{{{}}}".format(sum1 + " + " + sum2, end[0] - start[0])

    def string_spline(self):
        string = ""
        for i in range(self.n):
            string = (string + "$s_{{{}}} = {}$".format(i, self.string_polynomial(self.data_points[i], self.data_points[i + 1])) +
                      " for $x \\in [{}, {}]$\n\n".format(self.data_points[i][0], self.data_points[i + 1][0]))
        return string

    def plot_and_print(self):
        f, (ax1, ax2) = plt.subplots(1, 2)

        # plot the splines
        ax1.plot(*self.data_exact())
        ax1.plot(*self.data_spline())

        # auxilary lines to indicate the nodes
        for xi in np.linspace(*self.stg["range"], self.n + 1):
            ax1.axvline(xi, linestyle=":", color="black")

        ax1.set_title("Number of splines (n): {}\n(Number of nodes: {})".format(self.n, self.n + 1))

        # print the splines
        ax2.text(0.5, 0.5, self.string_spline(), horizontalalignment='center', verticalalignment='center', fontsize=24)
        ax2.axis('off')

        plt.show()

def main():
    """
    DEMONSTRATION.
    """
    def demonstration(f, n, stg=DEFAULT_SETTINGS):
        LSI = LinearSplineInterpolation(f, n, stg)
        LSI.plot_and_print()

    demonstration(lambda x: 1 + 3 * x ** 3 + 5 * x ** 5, 4)

    if False:
        # demonstration with x * sin(x)
        wider_range = {"range": [-10, 10], "fineness": 500}
        demonstration(lambda x: x * np.sin(x), 10, stg=wider_range)
        demonstration(lambda x: x * np.sin(x), 20, stg=wider_range)

        # demonstration with the Runge function
        def runge_function(x):
            return 1 / (1 + 25 * (x ** 2))

        for n in range(2, 22, 2):
            demonstration(runge_function, n)

        for n in range(3, 23, 2):
            demonstration(runge_function, n)

        for n in range(3, 23, 2):
            demonstration(runge_function, n, stg=wider_range)

if __name__ == "__main__":
    main()
