import re
from collections import Counter


def parse_counts(text: str):
    TOKEN_RE = re.compile(r"\b[a-zA-Z0-9]{5}\b")
    tokens = TOKEN_RE.findall(text)
    return Counter(tokens)


def test_parse_counts_basic():
    text = "asfga asdabasdjabsf _ _ _ has3l asd has3l"
    result = parse_counts(text)
    assert result["asfga"] == 1
    assert result["has3l"] == 2
    assert len(result) == 2


def test_parse_counts_sort():
    text = "aaaaa bbbbb aaaaa ccccc bbbbb aaaaa"
    result = parse_counts(text)
    sorted_items = sorted(result.items(), key=lambda x: -x[1])
    assert sorted_items[0][0] == "aaaaa"
    assert sorted_items[0][1] == 3
    assert sorted_items[1][0] == "bbbbb"
    assert sorted_items[1][1] == 2
    assert sorted_items[2][0] == "ccccc"
    assert sorted_items[2][1] == 1
