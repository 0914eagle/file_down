
from fractions import Fraction
s1, s2 = input(), input()
n = len(s1)
def solve(p, s):
    n = len(s)
    if n == 0:
        return Fraction(1, 2) ** p
    if s[0] == '?':
        return Fraction(1, 2) ** p * (solve(p + 1, s[1:]) + solve(p + 1, '-' + s[1:]))
    else:
        if s[0] == s1[0]:
            return Fraction(1, 2) ** p * solve(p + 1, s[1:])
        else:
            return Fraction(0)
print(solve(0, s2))
