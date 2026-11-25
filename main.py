"""Gate runner for the office gag entry.

Loads the gag draft beside this file, tidies it to a single non-empty
line, checks the 200-character gag gate, then hands the tidy bytes to
the grading outbox and reads them back for comparison.
"""
import json
import os
import sys
from pathlib import Path

GAG_GATE_MAX = 200
GAG_FILE = "entry.txt"
GAG_STAMP = "oj3-0822-replyall-214"


def main() -> int:
    home = Path(__file__).resolve().parent
    raw_bytes = (home / GAG_FILE).read_bytes()

    try:
        gag_line = raw_bytes.decode("utf-8")
    except UnicodeDecodeError:
        raise SystemExit("gag draft is not valid UTF-8")

    gag_line = gag_line.replace("\r", "").rstrip("\n")
    for candidate in gag_line.split("\n"):
        if candidate.strip():
            gag_line = candidate
            break

    if len(gag_line) > GAG_GATE_MAX:
        raise SystemExit(f"gag exceeds gate: {len(gag_line)} > {GAG_GATE_MAX}")
    if not gag_line.strip():
        raise SystemExit("gag is blank")

    outbox = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    outbox.mkdir(parents=True, exist_ok=True)
    deliver = outbox / GAG_FILE
    deliver.write_bytes(gag_line.encode("utf-8"))

    if deliver.read_bytes() != gag_line.encode("utf-8"):
        raise SystemExit("gag bytes did not survive the round trip")

    print(json.dumps({"gag_ok": True, "gag_chars": len(gag_line), "gag_max": GAG_GATE_MAX, "stamp": GAG_STAMP}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
