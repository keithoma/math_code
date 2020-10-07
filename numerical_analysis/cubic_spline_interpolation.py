#!/usr/bin/python

"""
6th of October 2020
"""

import matplotlib.pyplot as plt
import numpy as np

class CubicSplineInterpolation:
    def __init__(self, data_points):
        """
        data_points should be a list of lists containing exactly two elements
        """
        self.data_points = data_points
        self.n           = len(data_points) - 1

        # settings
        self.local_fineness = 100
    
    def solve_for_m(self):
        # start by constructing A
        A = np.zeros([self.n - 1, self.n + 1])
        print(A)

def main():
    """
    DEMONSTRATION.
    """
    CSI = CubicSplineInterpolation([[1, 2], [2, 3], [3, 4]])
    CSI.solve_for_m()
if __name__ == "__main__":
    main()
