
from collections import Counter
def solve(s):
    n = len(s)
    if n < 26:
        return -1
    counter = Counter(s)
    missing = 26 - counter['?']
    if missing > 0:
        for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if ch not in counter:
                counter[ch] = 1
                missing -= 1
                if missing == 0:
                    break
    if missing > 0:
        return -1
    res = ''
    for ch in s:
        if ch == '?':
            for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if counter[c] == 1:
                    res += c
                    counter[c] = 0
                    break
        else:
            res += ch
    return res

s = input()
print(solve(s))

