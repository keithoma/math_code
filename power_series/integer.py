""" Colection of small functions.
"""

# set pylint to allow variable names under three letters
# pylint: disable=C0103

# from typing import Union, List

import numpy as np # just for testing purposes

def gcd(a: int | list[int], b: None | int=None) -> int:
    """ Returns the greatest common divisor of two integers.
    """
    a, b = abs(a), abs(b)
    return gcd(b, a % b) if b else a

def lcm(a: int | list[int], b: None | int=None) -> int:
    """ Returns the least common multiple of two integers.
    """
    a, b = abs(a), abs(b)
    return a * b // gcd(a, b) if gcd(a, b) != 0 else 0

def _nth_test(n, a, b):
    """ Executes a single test of gcd() and lcm(). For internal use only.

    Args:
        n (int): the current count of tests
        a (int): an integer
        b (int): an integer

    Returns:
        (int): n from the argument incremented by 1
    """
    computed_gcd = gcd(a, b)
    true_gcd = np.gcd(a, b)

    computed_lcm = lcm(a, b)
    true_lcm = np.lcm(a, b)

    print("--------------------------------------------------")
    print("Test {n}:\n"
          "gcd({a}, {b}) = {computed_gcd}. Should be {true_gcd}.\n"
          "lcm({a}, {b}) = {computed_lcm}. Should be {true_lcm}".format(
              n=n, a=a, b=b,
              computed_gcd=computed_gcd, true_gcd=true_gcd,
              computed_lcm=computed_lcm, true_lcm=true_lcm))

    if computed_gcd != true_gcd:
        raise Exception("Something went wrong. Computed gcd doesn't match actual gcd.")

    if computed_lcm != true_lcm:
        raise Exception("Something went wrong. Computed lcm doesn't match actual lcm.")

    return n + 1

def _test(number_of_random_tests=100, interval=(-8, 9)):
    """ Executes a batch of tests. For internal use only.

    Args:
        number_of_random_tests (int): the number of random tests executed in a batch
        interval (tuple of int): two ints as a tuple, left value is inclusive, right value is
            exclusive

    Returns
    """
    # counter for n-th test
    n = 1

    # test gcd and lcm for random integers
    for _ in range(1, number_of_random_tests + 1):
        a = np.random.randint(-1e7, 1e7)
        b = np.random.randint(-1e7, 1e7)
        n = _nth_test(n, a, b)

    # test gcd and lcm for small integers
    for a in range(interval):
        for b in range(interval):
            n = _nth_test(n, a, b)

    print("--------------------------------------------------")
    return None

if __name__ == "__main__":
    NUMBER_OF_RANDOM_TESTS = 100
    INTERVAL = (-8, 9)
    _test(NUMBER_OF_RANDOM_TESTS, INTERVAL)
