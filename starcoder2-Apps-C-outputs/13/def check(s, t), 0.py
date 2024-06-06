
from itertools import combinations

s = input()

def check(s, t):
    if len(t) == 1:
        return True
    for i in range(len(s) - len(t) + 1):
        if s[i] == t[0]:
            if check(s[i + 1:], t[1:]):
                return True
    return False

def solve(s):
    res = 0
    for i in range(1, len(s) + 1):
        for t in combinations(s, i):
            if check(s, t):
                res += 1
    return res

print(solve(s))
