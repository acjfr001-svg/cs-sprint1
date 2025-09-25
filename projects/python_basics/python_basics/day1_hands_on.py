def normalize_whitespace(s: str) -> str:
    """Collapse runs of whitespace (space/tab/newline) to single spaces; strip ends."""
    # split() with no args splits on any whitespace and collapses runs; join with single spaces.
    return " ".join(s.split())

def every_nth(s: str, n: int) -> str:
    """Return every n-th character starting from index 0 (n<=0 -> empty string)."""
    if n <= 0:
        return ""
    return s[::n]

def take_until(lst, stop):
    """Return items from start up to (but not including) the first 'stop'; if absent, return lst."""
    for i, x in enumerate(lst):
        if x == stop:
            return lst[:i]
    return lst[:]  # not found → return whole list copy

def dedupe_preserve_order(lst):
    """Remove duplicates while preserving first-seen order."""
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

def two_sum_indices(nums, target):
    """Return (i,j) with i<j s.t. nums[i]+nums[j]==target; if none, return None."""
    seen = {}  # value -> index
    for j, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], j)
        seen[x] = j
    return None
