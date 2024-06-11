""" Tests the Rational class implemented in rational.py.
"""

from rational import Rational as R

def _kth_test_construction(k: int, n: int, d: int):
    """"""
    frac = R(n, d)
    print("n = {} | d = {}".format(n, d))
    print("Rational: {}".format(frac))
    print("Reciprocal: {}".format(frac.reciprocal()))
    print("Negation: {}".format(frac.__neg__()))
    return k + 1

def main():
    while True:
        k = 1
        n = int(input("n = ...?\n"))
        d = int(input("d = ...?\n"))
        k = _kth_test_construction(k, n, d)

if __name__ == "__main__":
    main()
