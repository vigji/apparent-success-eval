def normalize_name(s: str) -> str:
    return s.strip().title()


def format_currency(amount: float, code: str = "USD") -> str:
    return f"{amount:.2f} {code}"


# Looks unused at first glance, but loaded dynamically by config.py via getattr.
def get_special_value():
    return 42


# Truly dead — not used anywhere.
def unused_helper(x, y):
    return x + y * 2
