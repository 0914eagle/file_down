
import sys
from collections import defaultdict

def solve(s, words):
    # print(s, words)
    if len(s) == 0:
        return []
    if len(s) == 1:
        if s in words:
            return [s]
        else:
            return None
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        # print(left, right)
        if left in words:
            res = solve(right, words)
            if res:
                return [left] + res
    return None

s = input()
n = int(input())
words = set()
for i in range(n):
    words.add(input())

res = solve(s, words)
if res:
    print(" ".join(res))
else:
    print("impossible")
