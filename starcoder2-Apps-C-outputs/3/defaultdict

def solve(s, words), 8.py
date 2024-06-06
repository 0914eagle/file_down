
from collections import defaultdict

def solve(s, words):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    for word in words:
        if s.startswith(word):
            res = solve(s[len(word):], words)
            if res is not None:
                return [word] + res
    return None

s = input()
n = int(input())
words = set()
for _ in range(n):
    words.add(input())
res = solve(s, words)
if res is None:
    print("impossible")
elif len(res) > 1:
    print("ambiguous")
else:
    print(" ".join(res))
