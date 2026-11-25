"""Office joke lifter: lifts the joke past the check, sets it down in the output."""
STAMP = "onebug-11251142-oj3"
import json
import os
from pathlib import Path

DESK = Path(__file__).resolve().parent
WALL = 200
QUIP = ("HR asked why I listed Excel as my emergency contact. "
        "I said if that file closes unexpectedly, "
        "so does everyone in this building.")


def lift():
    tray = DESK / "entry.txt"
    body = tray.read_text(encoding="utf-8").strip()
    holds = bool(body) and len(body) <= WALL
    if holds:
        bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
        if bay:
            Path(bay).mkdir(parents=True, exist_ok=True)
            (Path(bay) / "entry.txt").write_bytes(tray.read_bytes())
    print(json.dumps({"holds": holds, "stamp": STAMP, "weight": len(body), "wall": WALL}))


if __name__ == "__main__":
    lift()
