#!/usr/bin/env python3
"""In-place sort of JSON files' keys in a directory."""

import argparse

import json
from pathlib import Path

def existing_file_path(path_str) -> Path:
    path = Path(path_str)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"{path_str}: does not exist")
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"{path_str}: is not a file")
    return path

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sort JSON keys in place across files."
    )
    parser.add_argument(
        "paths",
        type=existing_file_path,
        nargs="+",
        help="JSON file",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Number of spaces for JSON indentation (default: 4)",
    )
    args: argparse.Namespace = parser.parse_args()

    for file_path in args.paths:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                # json.load can return dict, list, str, int, etc.
                data: any = json.load(f)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=args.indent, sort_keys=True)
                f.write("\n")

        except (json.JSONDecodeError, PermissionError) as e:
            print(f"skipped {file_path}: {e}")


if __name__ == "__main__":
    main()
