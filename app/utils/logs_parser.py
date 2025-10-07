import re
from collections import Counter

TOKEN_RE = re.compile(r"\b[a-zA-Z0-9]{5}\b")


def parse_counts(text: str):
    tokens = TOKEN_RE.findall(text)
    return Counter(tokens)
