#!/usr/bin/python

"""
1st of July 2021
"""

class AlgebraicNumber():
    def __init__(self, _coeff, _basis):
        self.coeff = _coeff
        self.basis = _basis
    
    def string_latex(self):
        string = ""
        for i in range(len(self.basis)):
            string += str(self.coeff[i]) + " " + self.basis[i] + " + "
        return string

def main():
    coeff = [1, 2, 3]
    basis = ["sin(2pi)", "e^i", "75"]
    AN = AlgebraicNumber(coeff, basis)
    print(AN.string_latex())

if __name__ == "__main__":
    main()
