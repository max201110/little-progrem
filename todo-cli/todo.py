"""Dependency-free JSON todo list CLI."""
import argparse
import json
from pathlib import Path

DB = Path(__file__).with_name("todos.json")


def load():
    return json.loads(DB.read_text(encoding="utf-8")) if DB.exists() else []


def save(items):
    DB.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Tiny persistent todo list")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add"); add.add_argument("title")
    sub.add_parser("list")
    done = sub.add_parser("done"); done.add_argument("id", type=int)
    args = parser.parse_args(); items = load()
    if args.command == "add":
        items.append({"title": args.title, "done": False}); save(items)
        print(f"Added #{len(items)}: {args.title}")
    elif args.command == "list":
        if not items: print("No todos yet.")
        for i, item in enumerate(items, 1): print(f"{i}. [{'x' if item['done'] else ' '}] {item['title']}")
    elif args.command == "done":
        if not 1 <= args.id <= len(items): parser.error("todo id out of range")
        items[args.id - 1]["done"] = True; save(items); print("Completed.")


if __name__ == "__main__":
    main()
