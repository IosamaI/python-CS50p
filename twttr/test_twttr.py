import pytest
from twttr import shorten

def test_shorten_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("python") == "pythn"

def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("WORLD") == "WRLD"
    assert shorten("PYTHON") == "PYTHN"

def test_shorten_mixed_case():
    assert shorten("HeLLo") == "HLL"
    assert shorten("WoRLd") == "WRLd"
    assert shorten("PyThOn") == "PyThn"

def test_shorten_with_spaces():
    assert shorten("hello world") == "hll wrld"
    assert shorten("  hello  ") == "  hll  "

def test_shorten_no_vowels():
    assert shorten("hll") == "hll"
    assert shorten("wrld") == "wrld"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_with_numbers():
    assert shorten("hello123") == "hll123"
    assert shorten("12345") == "12345"
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"

def test_shorten_with_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("...python...") == "...pythn..."
    assert shorten("H3llo!") == "H3ll!"

if __name__ == "__main__":
    pytest.main()
