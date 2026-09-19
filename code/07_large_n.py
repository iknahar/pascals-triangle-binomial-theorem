"""Handling n values too big to build a triangle for."""
from math import comb, factorial, sqrt, pi, e


def stirling(n):
    return sqrt(2 * pi * n) * (n / e) ** n


def central_guess(n):
    # the middle of row 2n, without touching a single factorial
    return 4 ** n / sqrt(pi * n)


if __name__ == "__main__":
    print("Stirling's approximation")
    for n in (1, 2, 5, 10, 20, 50, 100):
        err = 100 * (stirling(n) - factorial(n)) / factorial(n)
        print(f"  n={n:3d}  off by {err:+7.3f}%   1/(12n) = "
              f"{100 / (12 * n):.3f}%")
    print()
    print("The middle of row 2n")
    for n in (5, 10, 20, 50, 100):
        exact, guess = comb(2 * n, n), central_guess(n)
        err = 100 * (guess - exact) / exact
        print(f"  n={n:3d}  exact {exact:.4e}  guess {guess:.4e}  "
              f"off by {err:.2f}%")
