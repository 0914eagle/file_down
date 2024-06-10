
"""


def solve(s):
    x, y = 0, 0
    for c in s:
        if c == "L":
            x -= 1
        elif c == "R":
            x += 1
        elif c == "U":
            y += 1
        elif c == "D":
            y -= 1
    if x == 0 and y == 0:
        return -1

    L, R = 0, 0
    while L < len(s) and s[L] != "L":
        L += 1
    while R < len(s) and s[R] != "R":
        R += 1

    if L == len(s) and R == len(s):
        return -1

    if x == 0:
        return L + 1, R + 1
    if y == 0:
        return R + 1, L + 1

    return -1


