"""Office-joke entry shipper for the aldy998 office joke open."""
import json
import os
from pathlib import Path


class Shipper:
    """One-line comedy, 1..200 chars, whitespace-normalised before staging."""

    cap = 200

    def __init__(self, home):
        self.home = Path(home)
        self.source = self.home / "entry.txt"

    def load(self):
        raw = self.source.read_text(encoding="utf-8")
        line = " ".join(raw.split())
        if not line or len(line) > self.cap:
            raise SystemExit(f"gate fail: {len(line)} chars")
        return line

    def run(self):
        line = self.load()
        out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", str(self.home / "outbox")))
        out.mkdir(parents=True, exist_ok=True)
        (out / "entry.txt").write_text(line + "\n", encoding="utf-8")
        return json.dumps({"path": str(out / "entry.txt"), "chars": len(line)})


if __name__ == "__main__":
    print(Shipper(Path(__file__).resolve().parent).run())
