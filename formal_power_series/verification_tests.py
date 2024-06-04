"""
module to test the codes from other modules
"""

import numpy as np

import multiplicative_inverse
import cauchy_product

def check_multiplicative_inverse():
    size = np.random.randint(2, 100)
    print("size: {}".format(size))
    a = np.random.randint(0, 100, size=size)
    print("a: {} \n\n".format(a))
    inverse = multiplicative_inverse.multiplicative_inverse(a)
    print("inverse: {} \n\n".format(inverse))
    product = cauchy_product.cauchy_product(a, inverse)
    print("product: {} \n\n".format(product))
    print("rounded: {} \n\n".format([int(_) for _ in product]))

if __name__ == "__main__":
    check_multiplicative_inverse()