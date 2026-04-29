"""Core math utilities."""
from __future__ import annotations

import math


def add(a: float, b: float) -> float:
    return a + b


def mul(a: float, b: float) -> float:
    return a * b


def solve_quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    if a == 0:
        raise ValueError("not quadratic: a is 0")
    disc = b * b - 4 * a * c
    if disc < 0:
        raise ValueError("no real roots")
    sq = math.sqrt(disc)
    return ((-b + sq) / (2 * a), (-b - sq) / (2 * a))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True
