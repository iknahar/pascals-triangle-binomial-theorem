"""Pull a single coefficient out without expanding anything."""
from math import comb
import sympy as sp

x = sp.symbols("x")


def coefficient_of(power, n, a, b):
    # term k carries x to the (n - k), so solve n - k = power
    k = n - power
    if k < 0 or k > n:
        return 0
    return comb(n, k) * a ** (n - k) * b ** k


if __name__ == "__main__":
    # the x^5 coefficient of (2x - 3)^12
    fast = coefficient_of(5, 12, 2, -3)
    slow = sp.expand((2 * x - 3) ** 12).coeff(x, 5)
    print("one line  ", fast)
    print("full expand", slow)
    print("agree:", fast == slow)
