#!/usr/bin/python

"""
2nd of July 2021

the rest is matter of scaling and finding the notes
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from numpy.lib.twodim_base import tri


class RenameLater():
    def __init__(self):
        self.domain = np.array([
            []
        ])


def triangulation(x, y):
    if x * y <= 0 and abs(x) + abs(y) < 1:
        return 1 - abs(x) - abs(y)
        # return 0
    elif x * y >= 0:
        return 1 - abs(x) if abs(x) > abs(y) else 1 - abs(y)
    return 0
    

def ploting():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.linspace(-1, 1, 500)
    Y = np.linspace(-1, 1, 500)
    X, Y = np.meshgrid(X, Y)

    Z = np.array([triangulation(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.ocean, linewidth=0, antialiased=True)

    plt.show()


def main():
    ploting()

if __name__ == "__main__":
    main()