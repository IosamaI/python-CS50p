import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello there") == 0
    assert value("hello, Newman") == 0
    assert value("  hello ") == 0

def test_value_h_but_not_hello():
    assert value("hey") == 20
    assert value("Hi there") == 20
    assert value("howdy") == 20
    assert value("  hi ") == 20

def test_value_other():
    assert value("good morning") == 100
    assert value("what's up?") == 100
    assert value("salutations") == 100
    assert value("yo") == 100

if __name__ == "__main__":
    pytest.main()
