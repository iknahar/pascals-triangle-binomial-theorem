"""Every identity in the article, checked over a range of n."""
from math import comb


def row_sum(n):
    return sum(comb(n, k) for k in range(n + 1))


def alternating_sum(n):
    # (-1)**k is +1 on even k and -1 on odd k
    return sum((-1) ** k * comb(n, k) for k in range(n + 1))


def hockey_stick(r, n):
    # walk down column r from row r to row n
    return sum(comb(i, r) for i in range(r, n + 1))


def vandermonde(m, p, r):
    return sum(comb(m, k) * comb(p, r - k) for k in range(r + 1))


def shallow_diagonal(d):
    # the slant that runs up and to the right
    return sum(comb(d - k, k) for k in range(d // 2 + 1))


if __name__ == "__main__":
    for n in range(1, 9):
        print(f"n={n}  sum={row_sum(n):4d}  2^n={2 ** n:4d}  "
              f"alternating={alternating_sum(n)}")
    print()
    print("hockey stick 1+3+6+10+15 =", hockey_stick(2, 6),
          "and C(7,3) =", comb(7, 3))
    print("vandermonde              =", vandermonde(7, 5, 4),
          "and C(12,4) =", comb(12, 4))
    print("shallow diagonals        =",
          [shallow_diagonal(d) for d in range(10)])
