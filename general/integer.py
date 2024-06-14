"""A colection of small functions.

Currently implemented:
* gcd(a, b): greatest common divisor of a and b or just a; both a and b can be an int or list
* lcm(a, b): least common multiple of a and b or just a; both a and b can be an int or list
"""

from typing import Union, Optional
import warnings

IntOrList = Union[int, list[int]]

def _int_gcd(a: int, b: int) -> int:
    """Computes the gcd of two integers."""
    while b:
        a, b = b, a % b
    return abs(a)

def _list_gcd(a: list[int]) -> int:
    """Computes the gcd of a list of integers."""
    if not a:
        raise ValueError("The list must contain at least one integer.")
    result = abs(a[0])
    for number in a[1:]:
        result = _int_gcd(result, abs(number))
    return result

def gcd(a: IntOrList, b: Optional[IntOrList]=None) -> int:
    """Computes the gcd of ints and lists."""
    # this function is supposed to be used with ints in both arguments or a list in the first
    # argument
    if isinstance(a, int) and isinstance(b, int):
        result = _int_gcd(a, b)
    elif isinstance(a, list) and b is None:
        result = _list_gcd(a)

    # the other combinations are also supported, but will give a warning
    elif isinstance(a, int) and isinstance(b, list):
        warnings.warn(
            "Improper usage of gcd(). a is a int and b is a list "
            "(expected int or None).",
            RuntimeWarning)
        result = _list_gcd([a] + b)
    elif isinstance(a, int) and b is None:
        warnings.warn(
            "Improper usage of gcd(). a is a int and b is None "
            "(expected int).",
            RuntimeWarning)
        result = abs(a)
    elif isinstance(a, list) and isinstance(b, int):
        warnings.warn(
            "Improper usage of gcd(). a is a list and b is an int "
            "(expected None).",
            RuntimeWarning)
        result = _list_gcd(a + [b])
    elif isinstance(a, list) and isinstance(b, list):
        warnings.warn(
            "Improper usage of gcd(). a is a list and b is an list "
            "(expected None).",
            RuntimeWarning)
        result = _list_gcd(a + b)

    elif not isinstance(a, int | list):
        print(type(a))
        raise TypeError("Invalid type for first argument. Expected int or list of int.")
    elif not isinstance(b, int | list | None):
        print(type(b))
        raise TypeError("Invalid type for second argument. Expected int or list of int.")

    return result  # pylint: disable=possibly-used-before-assignment

def _int_lcm(a: int, b: int) -> int:
    """Computes the least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // _int_gcd(a, b)

def _list_lcm(a: list[int]) -> int:
    """Computes the least common multiple of two lists."""
    if not a:
        return 0
    lcm_value = a[0]
    for num in a[1:]:
        lcm_value = _int_lcm(lcm_value, num)
    return lcm_value

def lcm(a: IntOrList, b: Optional[IntOrList]=None) -> int:
    """Computes the lcm of ints and lists."""
    # this function is supposed to be used with ints in both arguments or a list in the first
    # argument
    if isinstance(a, int) and isinstance(b, int):
        result = _int_lcm(a, b)
    elif isinstance(a, list) and b is None:
        result = _list_lcm(a)

    # the other combinations are also supported, but will give a warning
    elif isinstance(a, int) and isinstance(b, list):
        warnings.warn(
            "Improper usage of lcm(). a is a int and b is a list "
            "(expected int or None).",
            RuntimeWarning)
        result = _list_lcm([a] + b)
    elif isinstance(a, int) and b is None:
        warnings.warn(
            "Improper usage of lcm(). a is a int and b is None "
            "(expected int).",
            RuntimeWarning)
        result = abs(a)
    elif isinstance(a, list) and isinstance(b, int):
        warnings.warn(
            "Improper usage of lcm(). a is a list and b is an int "
            "(expected None).",
            RuntimeWarning)
        result = _list_lcm(a + [b])
    elif isinstance(b, list):
        warnings.warn(
            "Improper usage of lcm(). a is a list and b is an list "
            "(expected None).",
            RuntimeWarning)
        result = _list_lcm(a + b)

    elif not isinstance(a, int | list):
        raise TypeError("Invalid type for the first argument. Expected int or list of int.")
    elif not isinstance(b, int | list | None):
        raise TypeError("Invalid type for the second argument. Expected int or list of int.")

    return result  # pylint: disable=possibly-used-before-assignment

def main():
    """Tests the functions implemented."""
    print()
    print(f"_int_gcd(24, 300) = {_int_gcd(24, 300)}")
    print(f"_list_gcd(20, 100, 35) = {_list_gcd([20, 100, 35])}")
    print(f"gcd(13, 169) = {gcd(13, 169)}")
    print()
    print(f"_int_lcm(24, 300) = {_int_lcm(24, 300)}")
    print(f"_list_lcm(20, 100, 35) = {_list_lcm([20, 100, 35])}")
    print(f"lcm(13, 169) = {lcm(13, 169)}")
    print()

if __name__ == "__main__":
    main()
