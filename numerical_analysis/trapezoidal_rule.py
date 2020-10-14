import numpy as np

def trapezoidal_rule(a, b, f, n):
    h = (b - a) / n
    s = sum([f(a + i * h) for i in range(1, n)])
    return (1 / 2) * h * (f(a) + f(b) + 2 * s)

def simpsons_rule(a, b, f, n):
    h = (b - a) / n
    def x(i): return a + i * (b - a) / n
    s = sum([f(x(i - 1)) + 4 * f((x(i) - x(i - 1)) / 2) + f(x(i)) for i in range(1, n + 1)])
    return (h / 6) * s

def main():
    print(trapezoidal_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 6))
    print(simpsons_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 6))

if __name__ == "__main__":
    main()
