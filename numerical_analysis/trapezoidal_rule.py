import numpy as np

def trapezoidal_rule(a, b, f, n):
    h = (b - a) / n
    s = sum([f(a + i * h) for i in range(1, n)])
    return (1 / 2) * h * (f(a) + f(b) + 2 * s)

def main():
    print(trapezoidal_rule(0, 3, lambda x: np.sqrt(4 + x ** 3), 6))

if __name__ == "__main__":
    main()
