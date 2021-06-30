#!/usr/bin/python

from enum import Enum

class RNSetting():
    def __init__(self):
        self.reduction_mode = "auto"

class RationalNumber():
    def __init__(self, _sign, _num, _den, _setting=RNSetting()):
        self.sign         = _sign
        self.numerator    = _num
        self.denominator  = _den
        self.setting      = _setting

        if self.stg["handle"] == "auto":
            self.handle_sign()
            self.reduce_fraction()

    def handle_sign(self):
        def get_sign(x): return (1, -1)[x < 0]
        self.sign         = self.sign * get_sign(self.numerator) * get_sign(self.denominator)
        self.numerator    = int(abs(self.numerator))
        self.denominator  = int(abs(self.denominator))
        return self

    def reduce_fraction(self):
        def gcd(n, m): return n if m == 0 else gcd(m, n % m)
        div = gcd(self.numerator, self.denominator)
        self.numerator   = int(self.numerator / div)
        self.denominator = int(self.denominator / div)
        return self