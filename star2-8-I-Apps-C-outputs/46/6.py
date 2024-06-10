
from fractions import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def solve(m1, m2, m3, x1, x2, x3, y1, y2, y3):
    lcm12 = lcm(m1, m2)
    lcm123 = lcm(lcm12, m3)
    z = x1 * (lcm12 // m1) + x2 * (lcm12 // m2) + x3 * (lcm123 // m3)
    return z % lcm123

m1, m2, m3 = map(int, input().split())
x1, x2, x3 = map(int, input().split())
y1, y2, y3 = map(int, input().split())

print(solve(m1, m2, m3, x1, x2, x3, y1, y2, y3))


