
from math import factorial
def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
def solve(s1, s2):
    n = len(s1)
    if n != len(s2):
        return 0
    unrecognized = s2.count("?")
    nCorrect = 0
    for i in range(n):
        if s1[i] == s2[i] or s2[i] == "?":
            nCorrect += 1
    if nCorrect == n:
        return 1
    elif nCorrect < n:
        nIncorrect = n - nCorrect
        return sum([nCk(unrecognized, k) * 0.5 ** unrecognized for k in range(nIncorrect, unrecognized + 1)])

print(solve("++-+-", "+-??"))

