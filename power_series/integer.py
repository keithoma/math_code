""" Colection of small functions.
"""

# set pylint to allow variable names under three letters
# pylint: disable=C0103

# from typing import Union, List

import numpy as np # just for testing purposes

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

def int_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def list_gcd(a: list[int]) -> int:
    # Initialize the GCD with the first element 
    result = a[0]

    # Compute the GCD iteratively for each element in the list
    for number in a[1:]:
        result = int_gcd(result, number)

    return result

@log_decorator
def gcd(a: int | list[int], b: int | list[int] | None=None) -> int:
    """ Returns the greatest common divisor of two integers.
    """
    if isinstance(a, int) and isinstance(b, int):
        int_gcd(a, b)
    elif isinstance(a, int) and isinstance(b, list[int]):

    elif isinstance(a, int) and isinstance(b, None):
        return a
    elif isinstance(a, list) and isinstance(b, int):
        pass
    elif isinstance(a, list) and isinstance(b, list):
        pass
    elif isinstance(a, list) and isinstance(b, None):
        pass
    else:
        raise TypeError

    a, b = abs(a), abs(b)
    return gcd(b, a % b) if b else a

@log_decorator
def lcm(a: int | list[int], b: None | int=None) -> int:
    """ Returns the least common multiple of two integers.
    """
    a, b = abs(a), abs(b)
    return a * b // gcd(a, b) if gcd(a, b) != 0 else 0

@log_decorator
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

@log_decorator
def _test(number_of_random_tests: int=100, interval: tuple[int]=(-8, 9)):
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
