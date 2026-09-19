"""Build Pascal's triangle with nothing but addition."""


def pascal(nmax):
    # row 0 is a single 1, and every later row grows out of the one above
    rows = [[1]]
    for n in range(1, nmax + 1):
        prev = rows[-1]
        # add each entry to its right hand neighbour
        middle = [prev[i] + prev[i + 1] for i in range(len(prev) - 1)]
        # the outside edges are always 1, so bolt them on either side
        rows.append([1] + middle + [1])
    return rows


if __name__ == "__main__":
    for r in pascal(8):
        print(" ".join(str(v) for v in r).center(40))
