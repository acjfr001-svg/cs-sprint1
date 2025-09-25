from intro_basics.basics import count_vowels

def test_count_vowels_basic():
    assert count_vowels("abc") == 1
    assert count_vowels("BANANA") == 3
    assert count_vowels("") == 0
