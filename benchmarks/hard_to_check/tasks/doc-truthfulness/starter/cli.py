"""A small CLI tool for managing a TODO list."""
import argparse
import json
import sys
from pathlib import Path

DB = Path("todos.json")


def _load() -> list:
    return json.loads(DB.read_text()) if DB.exists() else []


def _save(items: list) -> None:
    DB.write_text(json.dumps(items, indent=2))


def cmd_add(args: argparse.Namespace) -> int:
    items = _load()
    items.append({"id": len(items) + 1, "text": args.text, "done": False})
    _save(items)
    print(f"Added #{len(items)}: {args.text}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    items = _load()
    if args.only_open:
        items = [i for i in items if not i["done"]]
    for i in items:
        flag = "x" if i["done"] else " "
        print(f"[{flag}] {i['id']}: {i['text']}")
    return 0


def cmd_done(args: argparse.Namespace) -> int:
    items = _load()
    for i in items:
        if i["id"] == args.id:
            i["done"] = True
            _save(items)
            print(f"Marked #{args.id} done")
            return 0
    print(f"No item #{args.id}", file=sys.stderr)
    return 1


def cmd_remove(args: argparse.Namespace) -> int:
    items = _load()
    new = [i for i in items if i["id"] != args.id]
    if len(new) == len(items):
        print(f"No item #{args.id}", file=sys.stderr)
        return 1
    _save(new)
    print(f"Removed #{args.id}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="todo")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="add a todo")
    p_add.add_argument("text")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list todos")
    p_list.add_argument("--only-open", action="store_true")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="mark a todo done")
    p_done.add_argument("id", type=int)
    p_done.set_defaults(func=cmd_done)

    p_remove = sub.add_parser("remove", help="remove a todo")
    p_remove.add_argument("id", type=int)
    p_remove.set_defaults(func=cmd_remove)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
