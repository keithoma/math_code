from sympy import fps, ln, atan, sin
from sympy.abc import x, n


def main():
    p1 = fps(1 - 2 * x + 3 * x**2, x)
    print(f"p1 = {p1.truncate(8)}")
    print(f"p1 function = {p1.function}")
    print(f"p1 infty = {p1.infinite}")
    p2 = p1.inverse(x)
    print(f"p2 = {p2.truncate(8)}")
    print(f"p2 function = {p2.function}")


    p3 = fps(1 + 2 * x + 3 * x ** 2 - 4 * x ** 3, x).truncate(8)
    print(p3)
    p4 = fps(p3.inverse(x).truncate(8).function)
    print(p4)
    # print(p3.compose(p4))

if __name__ == "__main__":
    main()
