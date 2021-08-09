#!/usr/bin/python

"""
9th of August 2021

A lot contains N items from which n items are chosen for examination. The lot is accepted if, among these n items, there are less than m defective items. Find the probability of accepting the lot if it contains M defective items.
"""

import random

class DefectiveItems():
    def __init__(self, _N, _M, _n, _m):
        self.N = _N
        self.M = _M
        self.n = _n
        self.m = _m

        self.lot = [False for _ in range(_M)] + [True for _ in range(_N - _M)]

    def experiment(self):
        random.shuffle(self.lot)
        print(self.lot)
        defective = 0
        for item in self.lot[:self.n]:
            if item is False:
                defective += 1
                if defective >= self.m:
                    return False
        return True

    def repeat_experiment(self, _rep):
        accepted = 0
        for _ in range(_rep):
            if self.experiment():
                accepted += 1
        return accepted

def main():
    DI = DefectiveItems(60, 36, 7, 4)
    print(DI.repeat_experiment(10000))

if __name__ == "__main__":
    main()
