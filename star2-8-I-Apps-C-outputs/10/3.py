
from math import log10, floor, ceil
def solve(a, b):
  def f(x):
    return sum(floor(log10(x)) + 1)
  return f(b) - f(a - 1)
q = int(input())
for _ in range(q):
  a, b = map(int, input().split())
  print(solve(a, b))

