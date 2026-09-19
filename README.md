# Pascal's Triangle and the Binomial Theorem

Runnable Python for the article *The Triangle That Does Your Algebra For You*.
Every number quoted in the article is produced by one of these scripts, so you
can check any claim yourself instead of taking my word for it.

## What is in here

| file | what it shows |
|---|---|
| `code/01_build_triangle.py` | Builds Pascal's triangle using only addition |
| `code/02_check_theorem.py` | Confirms the binomial theorem against brute force expansion, n = 1 to 12 |
| `code/03_one_coefficient.py` | Pulls one coefficient out of `(2x - 3)^12` without expanding |
| `code/04_identities.py` | Row sums, alternating sums, hockey stick, Vandermonde, shallow diagonals |
| `code/05_probability.py` | The binomial distribution, the "at least one" formula, and how the peak shrinks |
| `code/06_patterns.py` | Powers of eleven, and the fractal that appears in the odd entries |
| `code/07_large_n.py` | Stirling's approximation and the shortcut for the middle of a huge row |

## Running it

```bash
pip install sympy
python code/01_build_triangle.py
```

Only `02_check_theorem.py` and `03_one_coefficient.py` need sympy. The rest use
the standard library alone.

## Handy things to know

`math.comb(n, k)` arrived in Python 3.8. It computes binomial coefficients with
a loop that multiplies and divides as it goes, instead of building three giant
factorials and cancelling most of them away. That is why `math.comb(10**400, 200)`
returns an answer rather than eating your memory.

Avoid `scipy.special.comb` with `exact=False` for large inputs. It works in
floating point and will quietly hand you a slightly wrong integer.
