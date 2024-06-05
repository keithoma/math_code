"""
given two polynomials as two lists of coefficients, computes its formal product

References:
https://en.wikipedia.org/wiki/Formal_power_series#Ring_structure
"""



def cauchy_product(a, b, n=10):
    """
    """
    if len(a) > n: n = len(a)
    if len(b) > n: n = len(b)

    while len(a) < n: a.append(0)
    while len(b) < n: b.append(0)

    def c(k): return sum([a[l] * b[k - l] for l in range(k + 1)])

    return [c(k) for k in range(n)]




if __name__ == "__main__":
    print(cauchy_product([3, 0, 1], [0, -2, 0, 3]))

    import multiplicative_inverse

    print(cauchy_product([1, 6, 9], multiplicative_inverse.multiplicative_inverse([1, 6, 9])))
