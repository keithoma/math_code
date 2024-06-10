""" Colection of small functions.
"""

import numpy as np # just for testing purposes

def gcd(a, b):
    a, b = abs(a), abs(b)
    return gcd(b, a % b) if b else a

def lcm(a, b):
    a, b = abs(a), abs(b)
    return a * b // gcd(a, b) if gcd(a, b) != 0 else 0

if __name__ == "__main__":

    def nth_random_test(n, a, b):
        
        computed_gcd = gcd(a, b)
        true_gcd = np.gcd(a, b)
        
        computed_lcm = lcm(a, b)
        true_lcm = np.lcm(a, b)

        print("--------------------------------------------------")
        print("Test {n}:\n"
            "gcd({a}, {b}) = {computed_gcd}. Should be {true_gcd}.\n"
            "lcm({a}, {b}) = {computed_lcm}. Should be {true_lcm}".format(
                n = n, a = a, b = b, 
                computed_gcd = computed_gcd, true_gcd = true_gcd,
                computed_lcm = computed_lcm, true_lcm = true_lcm
                )
        )

        if computed_gcd != true_gcd:
            raise Exception("Something went wrong. Computed gcd doesn't match actual gcd.")
        
        if computed_lcm != true_lcm:
            raise Exception("Something went wrong. Computed lcm doesn't match actual lcm.")

        n = n + 1

        return n

    # counter for n-th test
    n = 1

    # test gcd and lcm for random integers
    number_of_random_tests = 100
    for _ in range(1, number_of_random_tests + 1):
        a = np.random.randint(-1e7, 1e7)
        b = np.random.randint(-1e7, 1e7)
        n = nth_random_test(n, a, b)

    print(lcm(0, 0))

    # test gcd and lcm for small integers
    for a in range(-8, 9):
        for b in range(-8, 9):
            n = nth_random_test(n, a, b)

    print("--------------------------------------------------")