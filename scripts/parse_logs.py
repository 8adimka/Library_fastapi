import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser(description="Count unique 5-char codes in a log file")
parser.add_argument("file", type=Path)
parser.add_argument("--sort", action="store_true", help="Sort by descending count")

TOKEN_RE = re.compile(r"\b[a-zA-Z0-9]{5}\b")


def count_tokens(path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for match in TOKEN_RE.findall(line):
                counts[match] = counts.get(match, 0) + 1
    return counts


def main():
    args = parser.parse_args()
    if not args.file.exists():
        parser.error(f"File not found: {args.file}")

    counts = count_tokens(args.file)
    items = sorted(counts.items(), key=lambda x: -x[1]) if args.sort else counts.items()

    for token, cnt in items:
        print(f"{token} : {cnt}")


if __name__ == "__main__":
    main()
