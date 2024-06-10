
from string import ascii_uppercase
def solve(s):
    missing = [c for c in ascii_uppercase if c not in s]
    if len(missing) > 26 - len(s):
        return -1
    res = []
    for c in s:
        if c == "?":
            res.append(missing.pop(0))
        else:
            res.append(c)
    return "".join(res)

s = input()
print(solve(s))

