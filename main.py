"""ofc6 reply-all desk. Steps run in order; each returns the ledger so far."""
import json
import os
import sys
from pathlib import Path

CEILING = 200


def read_line(root: Path):
    return root.joinpath("entry.txt").read_text(encoding="utf-8")


def judge(body: str):
    line = body.strip()
    fits = 1 <= len(line) <= CEILING and not line.isspace()
    return line, fits


def ship(line: str, fits: bool, ledger: dict):
    if fits:
        spot = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        spot.mkdir(parents=True, exist_ok=True)
        (spot / "entry.txt").write_bytes(line.encode("utf-8"))
        ledger["shipped_to"] = str(spot)
    ledger["fits"] = fits
    ledger["length"] = len(line)
    ledger["desk"] = "ofc6-replyall-r11251422"
    return ledger


def main():
    root = Path(__file__).resolve().parent
    ledger = {}
    raw = read_line(root)
    line, fits = judge(raw)
    report = ship(line, fits, ledger)
    print("VERDICT", json.dumps(report))
    return 0 if report["fits"] else 1


if __name__ == "__main__":
    sys.exit(main())
