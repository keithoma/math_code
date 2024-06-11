""" Tests the functions implemented in integer.py.
"""

from typing import Union, Optional

import numpy as np
import integer

IntOrList = Union[int, list[int]]

def _make_list(a: IntOrList, b: Optional[IntOrList]=None) -> list:
    """Combines the values of a and b to a single list."""
    if isinstance(a, int) and isinstance(b, int):
        result = [a, b]
    elif isinstance(a, int) and isinstance(b, list):
        result = [a] + b
    elif isinstance(a, int) and b is None:
        result = [a]
    elif isinstance(a, list) and isinstance(b, int):
        result = a + [b]
    elif isinstance(b, list):
        result = a + b
    elif isinstance(a, list) and b is None:
        result = a
    return result  # pylint: disable=possibly-used-before-assignment

def _nth_test(n: int, a: IntOrList, b: Optional[IntOrList]=None)  -> int:
    """Executes a single test of gcd() and lcm()."""
    computed_gcd = integer.gcd(a, b)
    computed_lcm = integer.lcm(a, b)
    true_gcd = np.gcd.reduce(_make_list(a, b))
    true_lcm = np.lcm.reduce(_make_list(a, b))

    print("--------------------------------------------------")
    print("Test {n}:\n"
          "gcd({a}, {b}) = {computed_gcd}. Should be {true_gcd}.\n"
          "lcm({a}, {b}) = {computed_lcm}. Should be {true_lcm}".format(
              n=n, a=a, b=b,
              computed_gcd=computed_gcd, true_gcd=true_gcd,
              computed_lcm=computed_lcm, true_lcm=true_lcm))

    if computed_gcd != true_gcd or computed_lcm != true_lcm:
        raise ValueError("Something went wrong. Computed value doesn't match the actual value.")

    return n + 1

# pylint: disable-next=useless-return
def _test(number_of_random_tests: int=100, interval: tuple[int, int]=(-8, 9)) -> None:
    """Executes a batch of tests. For internal use only."""
    # counter for n-th test
    n = 1

    # test gcd and lcm for random integers
    print("\n\n\nRANDOM INTEGER TEST\n\n\n")
    for _ in range(1, number_of_random_tests + 1):
        a = np.random.randint(-1e7, 1e7)
        b = np.random.randint(-1e7, 1e7)
        n = _nth_test(n, a, b)
    print("--------------------------------------------------")

    # brute force test for gcd and lcm with small integers
    print("\n\n\nBRUTE FORCE TEST\n\n\n")
    for a in range(*interval):
        for b in range(*interval):
            n = _nth_test(n, a, b)
    print("--------------------------------------------------")

    # test gcd and lcm for listsx
    # lcm grows rather quickly, be careful with the loop
    print("\n\n\nLIST TEST\n\n\n")
    for k in range(1, 11):
        a = np.random.randint(-1e2, 1e2, k).tolist()
        n = _nth_test(n, a)
    print("--------------------------------------------------")

    print("\n\n\nLIST TEST\n\n\n")
    for _ in range(1, number_of_random_tests + 1):
        match np.random.randint(1, 3):
            case 1: #int, int
                a = np.random.randint(-1e3, 1e3)
                b = np.random.randint(-1e3, 1e3)
            case 2: #int, list
                k = np.random.randint(1, 100)
                a = np.random.randint(-1e3, 1e3)
                b = np.random.randint(-10, 10, k).tolist()
            case 3: #int, None
                a = np.random.randint(-1e3, 1e3)
                b = None
            case 4: #list, int
                k = np.random.randint(1, 100)
                a = np.random.randint(-10, 10, k).tolist()
                b = np.random.randint(-1e3, 1e3)
            case 5: #list, list
                k = np.random.randint(1, 100)
                l = np.random.randint(1, 100)
                a = np.random.randint(-10, 10, k).tolist()
                b = np.random.randint(-10, 10, l).tolist()
            case 6: #list, None
                k = np.random.randint(1, 100)
                a = np.random.randint(-10, 10, k).tolist()
                b = None

        n = _nth_test(n, a, b)

    return None

def _warning_check():
    """Triggers all warnings."""
    print("The next ones should all throw a warning.")
    print()
    print(f"gcd(20, [100, 35]) = {integer.gcd(20, [100, 35])}")
    print(f"gcd(20) = {integer.gcd(20)}")
    print(f"gcd([20, 100], 35) = {integer.gcd([20, 100], 35)}")
    print(f"gcd([20], [100, 35]) = {integer.gcd([20], [100, 35])}")
    print()
    print(f"lcm(20, [100, 35]) = {integer.lcm(20, [100, 35])}")
    print(f"lcm(20) = {integer.lcm(20)}")
    print(f"lcm([20, 100], 35) = {integer.lcm([20, 100], 35)}")
    print(f"lcm([20], [100, 35]) = {integer.lcm([20], [100, 35])}")


def main(number_of_random_tests=100, interval=(-8, 9)):
    """Executes the tests."""
    _test(number_of_random_tests, interval)
    _warning_check()

if __name__ == "__main__":
    main()
