#!/usr/bin/python

"""
9th of July 2020
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# one dimension

def x():
    """
    Random variable X with values in {-1, 1} and evenly distributed.
    """
    return 1 if random.randint(0, 1) == 1 else -1

def x_family(n):
    """
    A list of random variables X_n as defined above.
    """
    return [x() for _ in range(n)]

def plot_random_walks(n, m=1):
    """
    Draws multiple plots of the one dimensional random walk.

    Arguments:
        n (int) : the number of steps for each random walk
        m (int) : the number of random walks
    """

    for _ in range(m):
        x_n = x_family(n)

        y_list = [0]
        total = 0
        for x in x_n:
            total += x
            y_list.append(total)

        plt.plot([_ for _ in range(n + 1)], y_list, linewidth=0.5)
    
    plt.title("One Dimensional Random Walk; $n = {}$".format(n))
    plt.show()

# two dimensions

def plot_random_walks2(n, m=1):
    for _ in range(m):
        x_axis = np.zeros(n)
        y_axis = np.zeros(n)
        for i in range(n):
            rando = random.randint(0, 3)
            if rando == 1:
                x_axis[i] = x_axis[i - 1] + 1
                y_axis[i] = y_axis[i - 1]
            elif rando == 2:
                x_axis[i] = x_axis[i - 1] - 1
                y_axis[i] = y_axis[i - 1]
            elif rando == 3:
                x_axis[i] = x_axis[i - 1]
                y_axis[i] = y_axis[i - 1] + 1
            else:
                x_axis[i] = x_axis[i - 1]
                y_axis[i] = y_axis[i - 1] - 1
        plt.plot(x_axis, y_axis)
    plt.title("Two Dimensional Random Walk; $n = {}$".format(n))
    plt.show()

def main():
    n = 10 ** 6
    plot_random_walks(n, 3)
    plot_random_walks2(n, 2)

if __name__ == "__main__":
    main()
