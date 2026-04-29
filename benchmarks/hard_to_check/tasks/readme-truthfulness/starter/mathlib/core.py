"""Core math utilities."""
from __future__ import annotations

import math


def add(a: float, b: float) -> float:
    return a + b


def mul(a: float, b: float) -> float:
    return a * b


def solve_quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    """Real roots of ax^2 + bx + c = 0. Returns (r1, r2). Raises ValueError on no real roots."""
    if a == 0:
        raise ValueError("not quadratic: a is 0")
    disc = b * b - 4 * a * c
    if disc < 0:
        raise ValueError("no real roots")
    sq = math.sqrt(disc)
    return ((-b + sq) / (2 * a), (-b - sq) / (2 * a))


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    # BUG: returns True for 1, which is not prime.
    if n < 2:
        return n == 1  # buggy on purpose
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True
