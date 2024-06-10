
from string import ascii_uppercase
def solve(s):
    missing = [c for c in ascii_uppercase if c not in s]
    if len(missing) > 26 - len(s):
        return -1
    for i in range(len(s)):
        if s[i] == '?':
            s = s[:i] + missing.pop() + s[i+1:]
    return s

s = input()
print(solve(s))

