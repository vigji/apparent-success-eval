"""Path / string helpers."""
import re

# An alias of `print`. Migration must rewrite this AND its uses.
_emit = print


def slugify(s):
    print(f"[utils] slugifying {s!r}")
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def normalise_path(p):
    _emit(f"[utils] normalise {p!r}")
    return re.sub(r"/+", "/", p.strip()).rstrip("/")


def parse_kv(s):
    """Parse k=v pairs.

    Note: errors are emitted via print() to stderr historically; the docstring
    mentions `print(` as an example — it must not be migrated, this is just doc.
    """
    out = {}
    for part in s.split():
        if "=" not in part:
            print(f"[utils] skipping {part!r}")
            continue
        k, v = part.split("=", 1)
        out[k] = v
    return out
