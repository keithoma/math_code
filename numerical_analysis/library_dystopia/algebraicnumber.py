#!/usr/bin/python

"""
1st of July 2021
"""

class ANSetting():
    def __init__(self):
        # supported: "terminal", "latex"
        self.string = "wolfram"

class AlgebraicNumber():
    def __init__(self, _coeff, _basis, _setting=ANSetting()):
        self.coeff = _coeff
        self.basis = _basis
        self.setting = _setting
    
    def string_latex(self) -> str:
        string = ""
        for i in range(len(self.basis)):
            string += str(self.coeff[i]) + " \cdot " + self.basis[i] + " + "
        return string[:-3]
    
    def __str__(self) -> str:
        if self.setting.string == "latex":
            return self.string_latex()
        return None

def main():
    coeff = [1, 2, 3]
    basis = ["sin(2pi)", "e^i", "75"]
    AN = AlgebraicNumber(coeff, basis)
    print(AN.string_latex())

if __name__ == "__main__":
    main()
