def normalize_whitespace(s: str) -> str:
    """Collapse runs of whitespace (space/tab/newline) to single spaces; strip ends."""
    raise NotImplementedError

def every_nth(s: str, n: int) -> str:
    """Return every n-th character starting from index 0 (n<=0 -> empty string)."""
    raise NotImplementedError

def take_until(lst, stop):
    """Return items from start up to (but not including) the first 'stop'; if absent, return lst."""
    raise NotImplementedError

def dedupe_preserve_order(lst):
    """Remove duplicates while preserving first-seen order."""
    raise NotImplementedError

def two_sum_indices(nums, target):
    """Return (i,j) with i<j s.t. nums[i]+nums[j]==target; if none, return None."""
    raise NotImplementedError
