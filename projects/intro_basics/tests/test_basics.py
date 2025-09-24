from intro_basics.basics import reverse_string

def test_reverse_string():
    # expected outputs (this is the spec)
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("racecar") == "racecar"
