"""Tiny CLI."""
import sys


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: app <name>", file=sys.stderr)
        return 1
    name = argv[1]
    print(f"hello, {name}!")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
