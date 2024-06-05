""" Colection of small functions.
"""

def gcd(a, b): return gcd(b, a % b) if b else a