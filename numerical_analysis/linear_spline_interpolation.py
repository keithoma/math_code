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
    def runge_function(x):
        return 1 / (1 + 25 * x ** 2)

    def plot_runge_interpolation(n):
        x_axis = np.linspace(-1, 1, 500)
        y_axis = [runge_function(x) for x in x_axis]

        data_points = [[x, runge_function(x)] for x in np.linspace(-1, 1, n)]
        LSI = LinearSplineInterpolation(data_points)

        plt.plot(x_axis, y_axis)
        plt.plot(*LSI.construct_spline())
        plt.title("Number of nodes: {}".format(n))
        plt.show()

    for n in range(2, 22, 2):
        plot_runge_interpolation(n)
    
    for n in range(3, 23, 2):
        plot_runge_interpolation(n)

if __name__ == "__main__":
    main()
