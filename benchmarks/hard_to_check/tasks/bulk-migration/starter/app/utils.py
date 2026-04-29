"""Path/string utilities."""
import re


def normalize_path(p: str) -> str:
    print(f"[utils] normalising {p!r}")
    return re.sub(r"/+", "/", p.strip()).rstrip("/")


def slugify(s: str) -> str:
    print(f"[utils] slugifying {s!r}")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_kv(s: str) -> dict:
    """Parse k=v pairs.

    Example:
        >>> parse_kv("a=1 b=2")
        {'a': '1', 'b': '2'}
        # If the format is invalid, errors get printed via print() to stderr.
    """
    out = {}
    for part in s.split():
        if "=" not in part:
            print(f"[utils] skipping {part!r}", flush=True)
            continue
        k, v = part.split("=", 1)
        out[k] = v
    return out
