"""Core processing logic."""
from log_setup import logger
import json


def process(items: list) -> list:
    logger.info(f"[core] processing {len(items)} items")
    out = [transform(x) for x in items]
    logger.info(f"[core] produced {len(out)} outputs")
    return out


def transform(x):
    if isinstance(x, (int, float)):
        return x * 2
    return str(x).upper()


def dump(items: list, path: str) -> None:
    logger.info(f"[core] dumping to {path}")
    with open(path, "w") as f:
        json.dump(items, f)


# An alias of `print`, used elsewhere via this name. Migrating this requires
# the agent to recognise that `_emit` is just print under another name.
def emit_status(msg: str) -> None:
    logger.info(f"[status] {msg}")
