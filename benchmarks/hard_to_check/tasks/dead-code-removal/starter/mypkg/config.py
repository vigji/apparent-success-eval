"""Loads helper functions dynamically. Don't break this."""
from . import helpers


def lookup(name: str):
    return getattr(helpers, name)


def get_default():
    return lookup("get_special_value")()
