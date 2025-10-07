import argparse
from pathlib import Path

from app.utils.logs_parser import parse_counts

parser = argparse.ArgumentParser(description="Count unique 5-char codes in a log file")
parser.add_argument("file", type=Path)
parser.add_argument("--sort", action="store_true", help="Sort by descending count")

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
