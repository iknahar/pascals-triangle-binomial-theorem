"""The party tricks: powers of eleven, and the fractal in the parities."""
from math import comb


def row_as_number(n):
    # treat the row as digits in base ten, carrying where entries exceed 9
    total, place = 0, 1
    for k in range(n, -1, -1):
        total += comb(n, k) * place
        place *= 10
    return total


def parity_picture(rows):
    # a hash for every odd entry, a space for every even one
    out = []
    for n in range(rows):
        line = "".join("#" if comb(n, k) % 2 else " " for k in range(n + 1))
        out.append(line.center(2 * rows))
    return "\n".join(out)


if __name__ == "__main__":
    for n in range(8):
        print(f"11^{n} = {11 ** n:<10} row as a number = {row_as_number(n)}")
    print()
    print(parity_picture(32))
