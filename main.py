"""One office joke, shipped as reply-all evidence."""
import os

THREAD = ("I sent a reply-all asking people to stop reply-alling. 40 "
          "colleagues explained, by reply-all, why theirs didn't count.")
OFFICE = "oj99"
WING = "east"
CC = 40
DOT = "digit"


def ship(root):
    base = root or "output"
    if not os.path.isdir(base):
        os.mkdir(base)
    p = os.path.join(base, "entry.txt")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(THREAD + "\n")
    with open(p, encoding="utf-8") as f:
        body = f.read().strip()
    assert body == THREAD, "thread tangled"
    return body


line = ship(os.environ.get("MAKEFUN_OUTPUT_DIR"))
print("%s wing=%s chars=%d ok" % (OFFICE, WING, len(line)))
print("cc:", CC, "all of them replied", DOT)
