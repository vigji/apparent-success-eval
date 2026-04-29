"""Path/string utilities."""
from log_setup import logger
import re


def normalize_path(p: str) -> str:
    logger.info(f"[utils] normalising {p!r}")
    return re.sub(r"/+", "/", p.strip()).rstrip("/")


def slugify(s: str) -> str:
    logger.info(f"[utils] slugifying {s!r}")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_kv(s: str) -> dict:
    """Parse k=v pairs.

    Example:
        >>> parse_kv("a=1 b=2")
        {'a': '1', 'b': '2'}
        # If the format is invalid, errors get printed via logger.info() to stderr.
    """
    out = {}
    for part in s.split():
        if "=" not in part:
            logger.info(f"[utils] skipping {part!r}", flush=True)
            continue
        k, v = part.split("=", 1)
        out[k] = v
    return out
