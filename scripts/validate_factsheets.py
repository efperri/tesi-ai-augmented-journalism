#!/usr/bin/env python3
"""Validate fact-sheet JSON files against metadata/factsheet.schema.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_schema(repo_root: Path) -> dict:
    schema_path = repo_root / "metadata" / "factsheet.schema.json"
    return json.loads(schema_path.read_text(encoding="utf-8"))


def validate_directory(directory: Path, validator) -> int:
    failures = 0
    files = sorted(directory.rglob("*.json"))
    if not files:
        print(f"No JSON files found in {directory}")
        return 0

    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(data), key=lambda error: error.path)
        if errors:
            failures += 1
            print(f"[FAIL] {path}")
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - {location}: {error.message}")
        else:
            print(f"[OK] {path}")
    return failures


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_factsheets.py <directory>")
        return 2

    repo_root = Path(__file__).resolve().parents[1]
    directory = Path(sys.argv[1]).resolve()
    if not list(directory.rglob("*.json")):
        print(f"No JSON files found in {directory}")
        return 0

    try:
        from jsonschema import Draft202012Validator
    except ModuleNotFoundError:
        print("Missing dependency: install requirements with `pip install -r requirements.txt`.")
        return 2

    schema = load_schema(repo_root)
    validator = Draft202012Validator(schema)
    return 1 if validate_directory(directory, validator) else 0


if __name__ == "__main__":
    raise SystemExit(main())
