"""
given a list of coefficients, computes the coefficients of the multiplicative inverse of a formal
power series

References:
https://en.wikipedia.org/wiki/Formal_power_series#Multiplicative_inverse
"""

def multiplicative_inverse(a):
    """
    Args:
        a (list)

    Returns:
        (list)
    """
    b = [1 / a[0]] # b_0 = 1 / a_0

    # after b_0, the coefficients are computed recursivly
    # b_n = - (1 / a_0) * sum_{i=1}^n a_i b_{n-i}
    def next(n): return - (1 / a[0]) * sum([a[i] * b[n - i] for i in range(1, n + 1)])

    for n in range(1, 11):
        b.append(next(n))
        print(b)

    return b

if __name__ == "__main__":
    print(multiplicative_inverse([1, 6, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

