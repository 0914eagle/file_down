
from collections import defaultdict
from sys import stdin

def solve(n, q, a, b):
  a.sort()
  a = list(set(a))
  n = len(a)
  dp = defaultdict(lambda: -1)
  dp[0] = 0
  for i in range(n):
    for j in range(a[i], b[-1] + 1):
      if dp[j - a[i]] != -1:
        dp[j] = min(dp[j], dp[j - a[i]] + 1) if dp[j] != -1 else dp[j - a[i]] + 1
  return [dp[x] for x in b]

n, q = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = [int(stdin.readline()) for _ in range(q)]
print(*solve(n, q, a, b))

