""" Tests the Rational class implemented in rational.py.
"""

from rational import Rational as R

def _kth_test_construction(k: int, n: int, d: int):
    """Executes a single test."""
    frac = R(n, d)
    print(f"n = {n} | d = {d}")
    print(f"Rational: {frac}")
    print(f"Reciprocal: {frac.reciprocal}")
    print(f"Negation: {-frac}")
    return k + 1

def main():
    """Executes the tests."""
    while True:
        k = 1
        n = int(input("n = ...?\n"))
        d = int(input("d = ...?\n"))
        k = _kth_test_construction(k, n, d)

if __name__ == "__main__":
    main()
