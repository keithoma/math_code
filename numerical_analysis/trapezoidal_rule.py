import numpy as np

def trapezoidal_rule(a, b, f, n):
    h = (b - a) / n
    s = sum([f(a + i * h) for i in range(1, n)])
    return (1 / 2) * h * (f(a) + f(b) + 2 * s)

def midpoint_rule(a, b, f, n):
    h = (b - a) / n
    def x(i): return a + i * h
    return h * sum([f((x(i) + x(i - 1)) / 2) for i in range(1, n + 1)])

def simpsons_rule(a, b, f, n):
    h = (b - a) / n
    def x(i): return a + i * h
    s = sum([f(x(i - 1)) + 4 * f((x(i) + x(i - 1)) / 2) + f(x(i)) for i in range(1, n + 1)])
    return (h / 6) * s

def main():
    print(trapezoidal_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 6))
    print(midpoint_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 6))
    print(simpsons_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 6))
    print()
    print(trapezoidal_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 20))
    print(midpoint_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 20))
    print(simpsons_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 20))
    print()
    print(trapezoidal_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 2))
    print(midpoint_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 2))
    print(simpsons_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 2))
    print()
    print(trapezoidal_rule(0, 3, lambda x: 3 * x + 5, 2))
    print(midpoint_rule(0, 3, lambda x: 3 * x + 5, 2))
    print(simpsons_rule(0, 3, lambda x: 3 * x + 5, 2))

if __name__ == "__main__":
    main()
