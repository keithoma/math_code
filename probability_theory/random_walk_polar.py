#!/usr/bin/python

"""
16th of August 2020
"""

import numpy as np
import matplotlib.pyplot as plt
import random

def generate_walk(n, start=(0, 0)):
    walk_x, walk_y       = [0 for _ in range(n)], [0 for _ in range(n)]
    walk_x[0], walk_y[0] = start
    for i in range(1, n):
        walk_x[i] = walk_x[i - 1] + np.cos(random.uniform(0, 2 * np.pi))
        walk_y[i] = walk_y[i - 1] + np.sin(random.uniform(0, 2 * np.pi))
    return walk_x, walk_y

def plot_walk(n):
    first_x, first_y = generate_walk(n)
    end = (first_x[n - 1], first_y[n - 1])
    second_x, second_y = generate_walk(n, end)
    end = (second_x[n - 1], second_y[n - 1])
    third_x, third_y = generate_walk(n, end)

    plt.plot(first_x, first_y)
    plt.plot(second_x, second_y)
    plt.plot(third_x, third_y)
    plt.show()

def main():
    plot_walk(10)

if __name__ == "__main__":
    main()