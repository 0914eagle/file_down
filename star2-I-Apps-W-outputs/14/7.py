
from fractions import Fraction
def solve(r, s, p):
    r, s, p = sorted([r, s, p])
    if r == s == p:
        return Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)
    elif r == s:
        return Fraction(r, r + p), Fraction(r, r + p), Fraction(p, r + p)
    elif r == p:
        return Fraction(r, r + s), Fraction(s, r + s), Fraction(r, r + s)
    elif s == p:
        return Fraction(r, r + s), Fraction(s, r + s), Fraction(r, r + s)
    elif r > s:
        return Fraction(r, r + s + p), Fraction(s, r + s + p), Fraction(p, r + s + p)
    else:
        return Fraction(r, r + s + p), Fraction(s, r + s + p), Fraction(p, r + s + p)

r, s, p = map(int, input().split())
print(*solve(r, s, p))

