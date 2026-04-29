"""Extras."""


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial of negative")
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def fib(n: int) -> int:
    if n < 0:
        raise ValueError("fib of negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
