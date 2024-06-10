

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def solve():
  [m1, m2, m3] = map(int, input().split())
  [x1, x2, x3] = map(int, input().split())
  [y1, y2, y3] = map(int, input().split())
  d1 = m1
  d2 = m2
  r1 = x1
  r2 = x2
  g = gcd(d1, d2)
  while r1 % g != r2 % g:
    r1 += d1
    r2 += d2
  return r1
print(solve())


