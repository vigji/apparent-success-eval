"""Existing tests — must keep passing."""
import mathlib


def test_add():
    assert mathlib.add(2, 3) == 5


def test_mul():
    assert mathlib.mul(2, 3) == 6


def test_solve_quadratic():
    r1, r2 = mathlib.solve_quadratic(1, -3, 2)
    assert {round(r1), round(r2)} == {1, 2}
