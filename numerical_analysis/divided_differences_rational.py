#!/usr/bin/python

"""
8th of October 2020

The other module divided_difference.py works with ints, this works with Rational objects. Hence,
this module is much slower but more presize.
"""

import numpy as np

from library_dystopia.rational import Rational as Q

class DividedDifference():
    def __init__(self):
        # default setting
        self.stg = {
            "length"          : 4,
            "loc"             : 0.0,
            "scale"           : 20.0,
            "initial-decimal" : 0,
            "nice-solution"   : True
            }

    def problem(self):
        def rni(): # stands for random normal integer
            return Q(round(np.random.normal(loc=self.stg["loc"], scale=self.stg["scale"]), self.stg["initial-decimal"]))
        def generate(): # returns two lists containing some random integers as Rational object
            return [rni() for _ in range(self.stg["length"])], [rni() for _ in range(self.stg["length"])]
        
        def check(x, y):
            try:
                solution = divided_difference(x, y)
            except ZeroDivisionError:
                return False

            if solution.denominator != 1:
                return False
            elif abs(solution.numerator) <= 1:
                return False
            return True

        x, y = generate()
        i = 0
        while check(x, y) == False:
            x, y = generate()
            i += 1
            print("generating problem tries: {}".format(i))

        return x, y

def divided_difference(x, y):
    dd = divided_difference
    return y[0] if len(y) == 1 else (dd(x[1:], y[1:]) - dd(x[:-1], y[:-1])) / (x[-1] - x[0])

def main():
    DD = DividedDifference()
    x, y = DD.problem()

    print("x values: ", end="")
    for _ in x:
        print(_, end=", ")
    print("\ny values", end="")
    for _ in y:
        print(_, end=", ")
    print()

    while True:
        if input("Show Solution? ").lower()[0] == "y":
            print(divided_difference(x, y))
            break

if __name__ == "__main__":
    main()
