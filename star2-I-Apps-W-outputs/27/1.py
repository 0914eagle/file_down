
from math import sqrt

def solve(n, b):
  b = [0] + b + [n - 1]
  res = []
  for i in range(1, n + 1):
    p1 = b[i - 1]
    p2 = b[i]
    if p1 < p2:
      res.append(p1)
    else:
      res.append(p2)
  return res

n = int(input())
b = list(map(int, input().split()))
res = solve(n, b)
print(" ".join(map(str, res)))

