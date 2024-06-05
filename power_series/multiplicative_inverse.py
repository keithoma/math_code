"""
given a list of coefficients, computes the coefficients of the multiplicative inverse of a formal
power series

References:
https://en.wikipedia.org/wiki/Formal_power_series#Multiplicative_inverse
"""

def multiplicative_inverse(a, n=10):
    """
    Args:
        a (list): the coefficients of a polynomial
        n (int): a natural number, we compute the coefficient of the multiplicative inverse up to n

    Returns:
        (list): the first n coefficients of the inverse
    """
    # to compute the first n coefficients of the inverse, we need to input the first n coefficients
    # from a, thus fill in the missing coefficients with 0s
    if len(a) > n: n = len(a)
    while len(a) < n: a.append(0)

    b = [1 / a[0]] # b_0 = 1 / a_0

    # after b_0, the coefficients are computed recursivly
    # b_n = - (1 / a_0) * sum_{i=1}^n a_i b_{n-i}
    def next_coefficient(n): return - (1 / a[0]) * sum([a[i] * b[n - i] for i in range(1, n + 1)])

    for k in range(1, n):
        b.append(next_coefficient(k))

    return b

if __name__ == "__main__":
    print(multiplicative_inverse([1, 6, 9]))

