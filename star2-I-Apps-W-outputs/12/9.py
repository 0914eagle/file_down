
from string import ascii_uppercase
def solve(s):
    missing = [c for c in ascii_uppercase if c not in s]
    if len(missing) > 0:
        for i in range(len(s)):
            if s[i] == '?':
                s = s[:i] + missing[0] + s[i+1:]
                missing = missing[1:]
                if len(missing) == 0:
                    break
    if len(missing) > 0:
        return -1
    for i in range(len(s)-25):
        window = s[i:i+26]
        if len(set(window)) == 26:
            return s
    return -1
s = input()
print(solve(s))

