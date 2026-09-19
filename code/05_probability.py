"""Where the binomial distribution formula comes from."""
from math import comb


def binomial_pmf(n, p):
    # one probability per possible number of successes, 0 through n
    return [comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]


def at_least_one(rate, tries):
    # easier to count the way it can go wrong, then flip it
    return 1 - (1 - rate) ** tries


if __name__ == "__main__":
    probs = binomial_pmf(8, 0.3)
    for k, v in enumerate(probs):
        print(f"{k} shots in   {v:.4f}")
    print("total", round(sum(probs), 12))
    print()
    for tries in (50, 100, 200, 300):
        print(f"1% rate, {tries:3d} tries   "
              f"{100 * at_least_one(0.01, tries):.1f}% chance of at least one")
    print()
    for n in (4, 10, 20, 100):
        peak = comb(n, n // 2) / 2 ** n
        print(f"{n:3d} coin flips   best single result {100 * peak:.2f}%")
