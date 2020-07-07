#!/usr/bin/python

"""
7th of July 2020
"""

import matplotlib.pyplot as plt
import random

# 1st dimension

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


def main():
    n = 10 ** 5
    plot_random_walks(n, 3)

if __name__ == "__main__":
    main()
