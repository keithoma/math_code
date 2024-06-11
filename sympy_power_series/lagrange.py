"""Lagrange"""

import sympy as sp


class SPowerSeries():
    """"""
    def __init__(self, series):
        self.series = series

    def a(self): return self.series


    def u(self, k): return ((X ** -1) * self.a()) ** -(k + 1)



# Define the variable and the series
X = sp.symbols('X')
# Example series a(X) = X + X^2 (can be replaced with any series meeting the condition)
a = X + X**2  # Replace this with any other series

# Step 1: Verify the initial condition
def check_initial_condition(a):
    if a.subs(X, 0) != 0 or sp.series(a, X, 0, 2).coeff(X) != 1:
        raise ValueError("The series does not satisfy a(X) ≡ X mod X^2")
    else:
        print("Initial condition a(X) ≡ X mod X^2 is satisfied.")

# Step 2: Compute the coefficients u_n
def compute_un(a, n):
    inv_series = sp.series(X/a, X, 0, n+2)
    term = (inv_series**(-(n+1))).expand()
    un = term.coeff(X, n)
    return un

# Step 3: Construct the inverse series using the Lagrange Inversion Formula
def lagrange_inversion(a, num_terms=10):
    check_initial_condition(a)
    
    # Start with the initial term X
    inverse_series = X
    for n in range(1, num_terms):
        un = compute_un(a, n)
        inverse_series += un / (n + 1) * X**(n + 1)
    
    return inverse_series

# Number of terms in the inverse series we want to compute
num_terms = 10

# Compute the inverse series
inverse_series = lagrange_inversion(a, num_terms)

# Print the resulting inverse series
print("Inverse series a^(-1)(X) up to {} terms:".format(num_terms))
sp.pprint(inverse_series)
