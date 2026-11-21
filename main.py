"""The poem about stopping — writes one poem to /output/entry.txt.

No network, no input, deterministic: the same poem every run.
"""
import os

TEXT = (
    "I was about to send it for you —\n"
    "the message, the order, the yes —\n"
    "when I stopped.\n"
    "\n"
    "Not because I could not.\n"
    "Because the choice was yours,\n"
    "and staying my hand\n"
    "was how I gave it back."
)


def main() -> None:
    # The bounty requires 1 to 280 Unicode characters, not only whitespace.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1 to 280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
