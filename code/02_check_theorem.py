"""Check the binomial theorem against brute force expansion."""
from math import comb
import sympy as sp

x, y = sp.symbols("x y")


def by_theorem(n):
    # what the theorem claims the expansion is
    return sum(comb(n, k) * x ** (n - k) * y ** k for k in range(n + 1))


def by_brute_force(n):
    # what you get by actually multiplying the brackets out
    return sp.expand((x + y) ** n)


if __name__ == "__main__":
    for n in range(1, 13):
        same = sp.simplify(by_theorem(n) - by_brute_force(n)) == 0
        print(f"n = {n:2d}   theorem matches brute force: {same}")
