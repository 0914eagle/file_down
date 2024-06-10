
from collections import Counter

def solve(s):
    missing = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if c not in s]
    if len(missing) == 0:
        return -1
    counter = Counter(s)
    for c in missing:
        if counter[c] > 0:
            return -1
    result = ''
    for c in s:
        if c == '?':
            result += missing.pop()
        else:
            result += c
    return result

s = input()
print(solve(s))

