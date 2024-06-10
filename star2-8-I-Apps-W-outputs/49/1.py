
from collections import Counter

def solve():
  n, k = map(int, input().split())
  h = list(map(int, input().split()))
  c = Counter(h)
  total = k ** n
  valid = 1
  for v in c.values():
    valid *= (k - 1) ** v
  return (total - valid) % 998244353

print(solve())

