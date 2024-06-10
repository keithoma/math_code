""" Colection of small functions.
"""

import numpy as np # just for testing purposes

def gcd(a, b):
    a, b = abs(a), abs(b)
    return gcd(b, a % b) if b else a

def lcm(a, b):
    a, b = abs(a), abs(b)
    return a * b // gcd(a, b)

if __name__ == "__main__":
    number_of_tests = 101
    for k in range(1, number_of_tests):
        a = np.random.randint(-1e7, 1e7)
        b = np.random.randint(-1e7, 1e7)
        
        computed_gcd = gcd(a, b)
        true_gcd = np.gcd(a, b)
        
        computed_lcm = lcm(a, b)
        true_lcm = np.lcm(a, b)

        print("--------------------------------------------------")
        print("Test {k}:\n"
            "gcd({a}, {b}) = {computed_gcd}. Should be {true_gcd}.\n"
            "lcm({a}, {b}) = {computed_lcm}. Should be {true_lcm}".format(
                k = k, a = a, b = b, 
                computed_gcd = computed_gcd, true_gcd = true_gcd,
                computed_lcm = computed_lcm, true_lcm = true_lcm
                )
        )

        if computed_gcd != true_gcd:
            break
    print("--------------------------------------------------")

