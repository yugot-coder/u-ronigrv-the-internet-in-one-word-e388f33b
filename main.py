"""scrollhole — The Internet in One Word.

Competition: u-ronigrv-the-internet-in-one-word-e388f33b
Task: describe the whole internet in a single word. The word must be
funny by itself, true about the internet as a whole (not one app, site
or mood), surprising, and short enough to land in one beat.

Final word (10 characters, gate is 1..30 characters):
    scrollhole

Why it wins: "scroll" is the one gesture every corner of the internet
shares — every feed, site and app — and "hole" is the rabbit hole you
fall into and cannot climb out of. One word, no explanation needed:
you came for one thing, you scrolled, and now it is three hours later.
It is a fresh portmanteau, not a word any competitor used, and it reads
instantly.

The program writes the word to entry.txt in MAKEFUN_OUTPUT_DIR
(default "/output") with no trailing newline, then re-reads the
written bytes to verify they match exactly, so the output is
deterministic across runs.
"""

import os

TEXT = "scrollhole"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    assert 1 <= len(data) <= 30, "entry must be 1..30 characters"
    assert data.strip(), "entry must not be only whitespace"
    assert b" " not in data and b"\n" not in data, "entry must be one word"
    with open(path, "wb") as f:
        f.write(data)
    verify_written_bytes(path, data)


def verify_written_bytes(path, data) -> None:
    """Re-read the written file and verify it byte-for-byte.

    The comparison is done on the SHA-256 digest of the landed bytes
    and raises SystemExit on mismatch, so the check also holds under
    `python -O` (where plain asserts are stripped).
    """
    import hashlib

    with open(path, "rb") as f:
        landed_bytes = f.read()
    landed = hashlib.sha256(landed_bytes).hexdigest()
    expected = hashlib.sha256(data).hexdigest()
    if landed != expected:
        raise SystemExit("read-back verification failed: entry.txt digest mismatch")


if __name__ == "__main__":
    main()
