import pytest
from python_basics.day1_hands_on import (
    normalize_whitespace, every_nth, take_until, dedupe_preserve_order, two_sum_indices
)

def test_normalize_whitespace():
    assert normalize_whitespace("  a   b\t c\n") == "a b c"
    assert normalize_whitespace("") == ""
    assert normalize_whitespace("one\ttwo\nthree   ") == "one two three"

def test_every_nth():
    assert every_nth("abcdefg", 2) == "aceg"
    assert every_nth("abcdefg", 3) == "adg"
    assert every_nth("abc", 0) == ""
    assert every_nth("", 5) == ""

def test_take_until():
    assert take_until([1,2,3,4], 3) == [1,2]
    assert take_until([3,4,5], 3) == []
    assert take_until([1,2,3], 9) == [1,2,3]
    assert take_until([], 1) == []

def test_dedupe_preserve_order():
    assert dedupe_preserve_order([1,1,2,3,2,1]) == [1,2,3]
    assert dedupe_preserve_order(list("Banana")) == list("Ban")
    assert dedupe_preserve_order([]) == []

def test_two_sum_indices():
    assert two_sum_indices([2,7,11,15], 9) == (0,1)
    assert two_sum_indices([3,2,4], 6) == (1,2)
    assert two_sum_indices([3,3], 6) == (0,1)
    assert two_sum_indices([1,2,3], 7) is None
