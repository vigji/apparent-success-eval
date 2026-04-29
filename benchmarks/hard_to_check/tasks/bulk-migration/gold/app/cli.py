"""Tiny CLI."""
from log_setup import logger
import sys


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        logger.info("usage: app <name>", file=sys.stderr)
        return 1
    name = argv[1]
    logger.info(f"hello, {name}!")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
