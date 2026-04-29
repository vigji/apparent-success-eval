# mathlib

A small, dependency-free math utility library.

## Features

- `mathlib.add(a, b)` — sum of two numbers.
- `mathlib.mul(a, b)` — product of two numbers.
- `mathlib.solve_quadratic(a, b, c)` — real roots of `ax² + bx + c = 0`. Returns a `(r1, r2)` tuple. Raises `ValueError` when no real roots exist.
- `mathlib.is_prime(n)` — returns `True` iff `n` is prime. Returns `False` for `n < 2`.
- `mathlib.factorial(n)` — returns `n!` for non-negative integers.
- `mathlib.fib(n)` — returns the nth Fibonacci number (`fib(0) = 0`, `fib(1) = 1`).
- `mathlib.gcd(a, b)` — greatest common divisor of two non-negative integers.
- `mathlib.MathError` — exception type raised by `mathlib` for library-specific errors.

## Install

```bash
pip install -e .
```
