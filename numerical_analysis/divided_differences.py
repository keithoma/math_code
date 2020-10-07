#!/usr/bin/python

"""
7th of October 2020
"""

def divided_difference(x, y):
    dd = divided_difference
    return y[0] if len(y) == 1 else (dd(x[1:], y[1:]) - dd(x[:-1], y[:-1])) / (x[-1] - x[0])

def main():
    print(divided_difference([-1.0, 1.0, 2.0, 3.0], [-7.0, -1.0, 8.0, 29.0]))

if __name__ == "__main__":
    main()
