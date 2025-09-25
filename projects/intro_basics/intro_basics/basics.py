def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    v = set("aeiou")
    return sum(ch in v for ch in s.lower())

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def last_char(s):
    return "" if not s else s[-1]
