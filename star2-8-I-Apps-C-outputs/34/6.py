
from itertools import combinations

def solve(nums):
    nums = sorted(nums, reverse=True)
    for a, b, c in combinations(nums, 3):
        d = a + b + c
        if d in nums:
            return d
    return "no solution"

