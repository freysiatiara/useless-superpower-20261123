"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line describing a hilariously useless
superpower to /output/entry.txt. Stdlib only, deterministic, no
network, no randomness.
"""

import os

LINE = "I can teleport anywhere instantly, but only to the exact spot I'm already standing in."


def main() -> None:
    # Self-checks: the gate requires UTF-8 text of 1-200 characters,
    # not only whitespace, in a single line.
    assert isinstance(LINE, str)
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Verify what was written, byte for byte.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written text differs from LINE"
    assert 1 <= len(written) <= 200
    print(f"wrote {len(written)} chars to /output/entry.txt")
    print(written)


if __name__ == "__main__":
    main()
