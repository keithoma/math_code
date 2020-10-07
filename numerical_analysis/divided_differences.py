#!/usr/bin/python

"""
7th of October 2020
"""

import numpy as np

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
        def generate():
            x_values = [round(np.random.normal(loc=self.stg["loc"], scale=self.stg["scale"]),
                        self.stg["initial-decimal"]) for _ in range(self.stg["length"])]
            y_values = [round(np.random.normal(loc=self.stg["loc"], scale=self.stg["scale"]),
                        self.stg["initial-decimal"]) for _ in range(self.stg["length"])]
            return x_values, y_values
    
        def check_solution_easy(x, y, decimals=1):
            try:
                return True if divided_difference(x, y).is_integer() else False
            except ZeroDivisionError:
                return False

        def check_solution_easy_nonzero(x, y, decimals=1):
            try:
                solution = divided_difference(x, y)
                return True if solution.is_integer() and solution != 0 else False
            except ZeroDivisionError:
                return False
        
        x, y = generate()

        i = 0
        if self.stg["nice-solution"] == True:
            while check_solution_easy_nonzero(x, y) == False:
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
    print("x values: {}".format(x))
    print("y values: {}".format(y))
    
    while True:
        if input("Show Solution? ").lower()[0] == "y":
            print(divided_difference(x, y))
            break


if __name__ == "__main__":
    main()
