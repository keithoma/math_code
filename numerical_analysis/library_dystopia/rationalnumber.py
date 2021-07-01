#!/usr/bin/python

"""
1st of July 2021
"""

class RNSetting():
    def __init__(self):
        self.reduction = "auto"
        # supported: "terminal", "latex"
        self.string = "latex"

class RationalNumber():
    def __init__(self, _num, _den, _sgn=1, _setting=RNSetting()):
        self.sgn = _sgn
        self.num = _num
        self.den = _den
        self.setting = _setting

        if self.setting.reduction == "auto":
            self.handle_all()

    def handle_sign(self):
        def get_sign(x): return (1, -1)[x < 0]
        self.sgn = self.sgn * get_sign(self.num) * get_sign(self.den)
        self.num = int(abs(self.num))
        self.den = int(abs(self.den))
        return self

    def reduce_fraction(self):
        def gcd(n, m): return n if m == 0 else gcd(m, n % m)
        div = gcd(self.num, self.den)
        self.num = int(self.num / div)
        self.den = int(self.den / div)
        return self

    def handle_all(self):
        self.handle_sign()
        self.reduce_fraction()
        return self

    def string_terminal(self):
        return "{s} {n} / {d}".format(s="-" if self.sgn < 0 else "", n=self.num, d=self.den)
    def string_latex(self):
        return "{s}\\frac{{{n}}}{{{d}}}".format(s="-" if self.sgn < 0 else "", n=self.num, d=self.den)

    def __str__(self):
        if self.setting.string == "terminal":
            return self.string_terminal()
        elif self.setting.string == "latex":
            return self.string_latex()
        else:
            return None

    def __add__(self, other):
        n = self.sgn * self.num * other.den + other.sgn * other.num * self.den
        d = self.den * other.den
        return RationalNumber(n, d).handle_all()

    def __sub__(self, other):
        n = self.sgn * self.num * other.den - other.sgn * other.num * self.den
        d = self.den * other.den
        return RationalNumber(n, d).handle_all()

    def __mul__(self, other):
        return RationalNumber(self.num * other.num, self.den * other.den, self.sgn * other.sgn)

    def __truediv__(self, other):
        return RationalNumber(self.num * other.den, self.den * other.num, self.sgn * other.sgn)


def main():
    R1 = RationalNumber(1, 3, -1)
    R2 = RationalNumber(3, 5)
    print(R1)
    print()
    print(R2)
    print()
    print(R1 + R2)
    print(R1 - R2)
    print(R1 + R1 + R1)
    print(R1 * R2)
    print()
    print(R1 / R2)

if __name__ == "__main__":
    main()
