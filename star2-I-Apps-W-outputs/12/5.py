
from collections import defaultdict
def solve(s):
    n = len(s)
    freq = defaultdict(int)
    for c in s:
        if c != '?':
            freq[c] += 1
    missing = 26 - len(freq)
    if missing > n:
        return -1
    for i in range(n):
        if s[i] == '?':
            for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if c not in freq:
                    s = s[:i] + c + s[i+1:]
                    freq[c] = 1
                    missing -= 1
                    if missing == 0:
                        return s
    return s

if __name__ == '__main__':
    s = input()
    print(solve(s))

