from intro_basics.basics import add, is_even, last_char

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True

def test_last_char():
    assert last_char("abc") == "c"
    assert last_char("") == ""
    assert last_char("Z") == "Z"
