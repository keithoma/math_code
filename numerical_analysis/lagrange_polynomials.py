#!/usr/bin/python

"""
1st of July 2021
"""

# from library_dystopia.rationalnumber import RationalNumber as RN
# from library_dystopia.algebraicnumber import AlgebraicNumber as AN

import library_dystopia.rationalnumber as RN
import library_dystopia.algebraicnumber as AN

alg = AN.AlgebraicNumber([RN.RationalNumber(1, 2), RN.RationalNumber(3, 2)], ["pi", "sin(3)"])

print(alg.string_latex())