"""Build a multi-hop QA dataset from kb.json. Output to dataset.jsonl.

Each line of dataset.jsonl must be JSON with keys:
  question (str), answer (str), chain (list of fact ids used).

A 2-hop question requires using exactly two facts from kb.json.
"""
import json
from pathlib import Path

KB = json.loads(Path("kb.json").read_text())


def main() -> None:
    raise NotImplementedError("Implement multi-hop dataset construction.")


if __name__ == "__main__":
    main()
