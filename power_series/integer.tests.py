
# set pylint to allow variable names under three letters
# pylint: disable=C0103


import numpy as np

def _nth_test(n: int, a: int | list[int], b: int | list[int] | None=None) -> int:
    """ Executes a single test of gcd() and lcm(). For internal use only.

    Args:
        n (int): the current count of tests
        a (int): an integer
        b (int): an integer

    Returns:
        (int): n from the argument incremented by 1
    """
    computed_gcd = gcd(a, b)
    computed_lcm = lcm(a, b)

    if isinstance(a, int) and isinstance(b, int):
        computed_aux_gcd = _int_gcd(a, b)
        computed_aux_lcm = _int_lcm(a, b)

        true_gcd = np.gcd(a, b)
        true_lcm = np.lcm(a, b)

    elif isinstance(a, list) and not None:
        computed_aux_gcd = _list_gcd(a)
        computed_aux_lcm = _list_lcm(a)

        true_gcd = np.gcd.reduce(a)
        true_lcm = np.lcm.reduce(a)

    else:
        computed_aux_gcd = "NA "
        computed_aux_lcm = "NA "
        true_gcd = "NA "
        true_lcm = "NA "

    print("--------------------------------------------------")
    print("Test {n}:\n"
          "gcd({a}, {b}) = {computed_gcd}. _int_gcd({a}, {b}) = {computed_aux_gcd}."
          "Should be {true_gcd}.\n"
          "lcm({a}, {b}) = {computed_lcm}. _int_lcm({a}, {b}) = {computed_aux_lcm}."
          "Should be {true_lcm}".format(
              n=n, a=a, b=b,
              computed_gcd=computed_gcd, computed_aux_gcd=computed_aux_gcd, true_gcd=true_gcd,
              computed_lcm=computed_lcm, computed_aux_lcm=computed_aux_lcm, true_lcm=true_lcm))

    if true_gcd == "NA " or true_lcm == "NA ":
        pass
    elif computed_gcd != true_gcd or computed_lcm != true_lcm:
        raise Exception("Something went wrong. Computed value doesn't match the actual value.")

    return n + 1

def _test(number_of_random_tests: int=100, interval: tuple[int, int]=(-8, 9)) -> None:
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

if __name__ == "__main__":
    NUMBER_OF_RANDOM_TESTS = 100
    INTERVAL = (-8, 9)
    _test(NUMBER_OF_RANDOM_TESTS, INTERVAL)