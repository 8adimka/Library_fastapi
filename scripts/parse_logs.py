import argparse
import re
from collections import Counter
from pathlib import Path

parser = argparse.ArgumentParser(description="Count unique 5-char codes in a log file")
parser.add_argument("file", type=Path)
parser.add_argument("--sort", action="store_true", help="Sort by descending count")


def parse_counts(text: str):
    TOKEN_RE = re.compile(r"\b[a-zA-Z0-9]{5}\b")
    tokens = TOKEN_RE.findall(text)
    return Counter(tokens)


args = parser.parse_args()

if not args.file.exists():
    print("File not found:", args.file)
    raise SystemExit(1)

text = args.file.read_text(encoding="utf-8", errors="ignore")
counts = parse_counts(text)

items = list(counts.items())
if args.sort:
    items.sort(key=lambda x: -x[1])

for tok, cnt in items:
    print(f"{tok} : {cnt}")
