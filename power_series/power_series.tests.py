""" Tests the functions implemented in integer.py.
"""
import numpy as np
from power_series import PowerSeries as PS

def magic_method_pow_test(ps: PS, k: int) -> None:
    """Executes a single test using the __pow__ method of PS."""
    print(f"a      = {ps}")
    print()
    print(f"a ** k = {ps ** k}")
    return None

def main():
    """Tests the functions from power_series.py."""
    a = np.random.randint(-3, 3, 3)
    magic_method_pow_test(PS(a), 3)

if __name__ == "__main__":
    main()
