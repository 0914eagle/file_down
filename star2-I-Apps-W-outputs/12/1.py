
from collections import Counter

def solve(s):
    s = list(s)
    missing = [i for i, c in enumerate(s) if c == '?']
    if len(missing) > 26:
        return -1
    counter = Counter(c for c in s if c != '?')
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if c not in counter:
            s[missing.pop()] = c
    return ''.join(s)

if __name__ == '__main__':
    s = input()
    print(solve(s))

