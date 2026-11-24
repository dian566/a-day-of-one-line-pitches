#!/usr/bin/env python3
"""Second pitch for make.fun: Uber for naps."""

# Bowo's pick: nap-sharing, with a contract against waking up.

import os

PITCH = "Uber for naps: a stranger's couch, a 20-minute timer, and a legally binding do-not-wake-me sign."


def pitch_it() -> None:
    """Write Bowo's nap pitch to /output/entry.txt, nothing else."""
    if len(PITCH) > 165 or not PITCH.strip():
        raise ValueError("pitch must be a non-empty line of at most 165 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":  # run it
    pitch_it()
