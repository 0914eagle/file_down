
from itertools import permutations

s = input()
n = int(input())
words = set()
for _ in range(n):
    words.add(input())

def check(s, words):
    s = s.replace(" ", "")
    for p in permutations(s):
        p = "".join(p)
        if p in words:
            return p
    return None

ans = []
for i in range(len(s)):
    if s[i] == " ":
        ans.append(" ")
        continue
    t = s[:i] + s[i+1:]
    res = check(t, words)
    if res is not None:
        ans.append(res[i])

ans = "".join(ans)
if ans in words:
    print(ans)
else:
    print("impossible")
