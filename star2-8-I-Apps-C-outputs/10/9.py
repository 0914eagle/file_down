
import sys
from bisect import bisect_left, bisect_right

def solve(q):
    for _ in range(q):
        a, b = map(int, sys.stdin.readline().split())
        left = bisect_left(nums, a)
        right = bisect_right(nums, b)
        print(right - left)

nums = list(set([i for i in range(1, 10**6 + 1)] + [int(str(n)[::-1]) for n in range(1, 10**6 + 1)]))
nums.sort()
solve(int(sys.stdin.readline()))

