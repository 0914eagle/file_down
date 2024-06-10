
import sys
import math
from itertools import permutations

def calc(xs, ys, ts, m):
  v = 0
  for i in range(n):
    x, y, t = xs[i], ys[i], ts[i]
    if math.fabs(x) + math.fabs(y) < math.fabs(xs[m - 1]) + math.fabs(ys[m - 1]):
      v += 1
  return v

def solve(xs, ys, ts, m):
  if m == 1:
    return calc(xs, ys, ts, m)
  else:
    return min(solve(xs, ys, ts, m - 1) + calc(xs, ys, ts, m), solve(xs, ys, ts, m - 1) + calc(xs, ys, ts, m - 1))

n, m = map(int, input().split())
xs = []
ys = []
ts = []
for i in range(n):
  x, y, t = map(int, input().split())
  xs.append(x)
  ys.append(y)
  ts.append(t)

print(solve(xs, ys, ts, m))

