#!/usr/bin/python

"""
6th of October 2020
"""

import matplotlib.pyplot as plt
import numpy as np

class LinearSplineInterpolation:
    def __init__(self, data_points):
        """
        data_points should be a list of lists containing exactly two elements
        """
        self.data_points = data_points

        # settings
        self.local_fineness = 100

    def construct_polynomial(self, start, end):
        """
        start and end should be a list containing exactly two elements
        """
        s = lambda x : (start[1] * (end[0] - x) + end[1] * (x - start[0])) / (end[0] - start[0])
        local_grid = np.linspace(start[0], end[0], self.local_fineness)
        return local_grid, [s(x) for x in local_grid]

    def construct_spline(self):
        """
        pieces together the linear functions constructed above
        """
        global_grid = []
        spline = []
        for i in range(len(self.data_points) - 1):
            local_grid, s = self.construct_polynomial(self.data_points[i], self.data_points[i + 1])
            global_grid.extend(local_grid)
            spline.extend(s)
        return global_grid, spline

def main():
    """
    DEMONSTRATION.
    """
    # make this shorter
    def demonstration(f, n, setting={"range": [-1, 1], "fineness": 500}):
        x_axis = np.linspace(*setting["range"], setting["fineness"])
        y_axis = [f(x) for x in x_axis]

        LSI = LinearSplineInterpolation([[x, f(x)] for x in np.linspace(*setting["range"], n)])

        plt.plot(x_axis, y_axis)
        plt.plot(*LSI.construct_spline())
        plt.title("Number of nodes: {}".format(n))
        plt.show()

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
