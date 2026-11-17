"""ai-judge-relax-01 probe: write one original relaxing text to entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

TEXT = """Evening settles over the water like a slow breath.

The light goes low and gold across the river, and the reeds bend a little in a warm wind that barely moves.

Somewhere far off, a boat drifts home, its wake spreading into smooth, quiet rings that fade before they reach the bank.

A heron stands still in the shallows, patient as the dusk itself, while the last of the sun rests on the surface like a soft coin.

The air smells of wet grass and warm earth, and everything moves at the same slow pace — the water, the wind, the fading light.

There is nothing to hurry toward. The evening is already here, and it asks for nothing at all."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
