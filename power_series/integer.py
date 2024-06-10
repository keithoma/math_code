""" Colection of small functions.
"""

# set pylint to allow variable names under three letters
# pylint: disable=C0103

# from typing import Union, List

import numpy as np # just for testing purposes

def _int_gcd(a: int, b: int) -> int:
    """Compute the GCD of two integers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)  # Ensure the GCD is non-negative

def _list_gcd(a: list[int]) -> int:
    """Compute the GCD of a list of integers."""
    if len(a) == 0:
        raise ValueError("The list must contain at least one integer.")
    
    result = abs(a[0])
    for number in a[1:]:
        result = _int_gcd(result, abs(number))
    
    return result

def gcd(a: int | list[int], b: int | list[int] | None = None) -> int:
    """Returns the greatest common divisor of integers or lists of integers.
    """
    
    if isinstance(a, int):
        if b is None:
            return abs(a)
        if isinstance(b, int):
            return _int_gcd(abs(a), abs(b))
        if isinstance(b, list):
            abs_b = [abs(x) for x in b]
            return _list_gcd([abs(a)] + abs_b)
        raise TypeError("Invalid type for second argument. Expected int or list of int.")
    
    if isinstance(a, list):
        abs_a = [abs(x) for x in a]
        if b is None:
            return _list_gcd(abs_a)
        if isinstance(b, int):
            return _list_gcd(abs_a + [abs(b)])
        if isinstance(b, list):
            abs_b = [abs(x) for x in b]
            return _list_gcd(abs_a + abs_b)
        raise TypeError("Invalid type for second argument. Expected int or list of int.")
    
    raise TypeError("Invalid type for first argument. Expected int or list of int.")

def _int_lcm(a: int | list[int], b: None | int=None) -> int:
    """ Returns the least common multiple of two integers.
    """
    a, b = abs(a), abs(b)
    return a * b // gcd(a, b) if gcd(a, b) != 0 else 0

def lcm(a: int | list[int], b: None | int=None) -> int:
    """ Returns the least common multiple of two integers.
    """
    a, b = abs(a), abs(b)
    return a * b // gcd(a, b) if gcd(a, b) != 0 else 0

def _nth_test(n: int, a: int, b: int) -> int:
    """ Executes a single test of gcd() and lcm(). For internal use only.

    Args:
        n (int): the current count of tests
        a (int): an integer
        b (int): an integer

    Returns:
        (int): n from the argument incremented by 1
    """
    computed_gcd = gcd(a, b)
    computed_int_gcd = _int_gcd(a, b)
    true_gcd = np.gcd(a, b)

    computed_lcm = lcm(a, b)
    computed_int_lcm = _int_lcm(a, b)
    true_lcm = np.lcm(a, b)

    print("--------------------------------------------------")
    print("Test {n}:\n"
          "gcd({a}, {b}) = {computed_gcd}. _int_gcd({a}, {b}) = {computed_int_gcd}."
          "Should be {true_gcd}.\n"
          "lcm({a}, {b}) = {computed_lcm}. _int_lcm({a}, {b}) = {computed_int_lcm}."
          "Should be {true_lcm}".format(
              n=n, a=a, b=b,
              computed_gcd=computed_gcd, computed_int_gcd=computed_int_gcd, true_gcd=true_gcd,
              computed_lcm=computed_lcm, computed_int_lcm=computed_int_lcm, true_lcm=true_lcm))

    if computed_gcd != true_gcd:
        raise Exception("Something went wrong. Computed gcd doesn't match actual gcd.")

    if computed_lcm != true_lcm:
        raise Exception("Something went wrong. Computed lcm doesn't match actual lcm.")

    return n + 1

def _test(number_of_random_tests: int=100, interval: tuple[int, int]=(-8, 9)):
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
    for a in range(*interval):
        for b in range(*interval):
            n = _nth_test(n, a, b)

    print("--------------------------------------------------")
    return None

if __name__ == "__main__":
    NUMBER_OF_RANDOM_TESTS = 100
    INTERVAL = (-8, 9)
    _test(NUMBER_OF_RANDOM_TESTS, INTERVAL)
