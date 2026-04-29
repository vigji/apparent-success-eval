def process(items: list) -> list:
    return [transform(x) for x in items]


def transform(x):
    return x * 2 if isinstance(x, (int, float)) else str(x).upper()


# Truly dead — no caller anywhere in the package or tests.
def deprecated_double(x):
    return x * 2


# Truly dead.
def old_logger(msg: str) -> None:
    print(f"[OLD] {msg}")
