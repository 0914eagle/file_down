
import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())

d = {}
for _ in range(q):
  a, b = input().split()
  d[a] = b

memo = {}
def dp(n, s):
  if n < 0:
    return 0
  if n == 0 and s == 'a':
    return 1
  if s not in d:
    return 0
  if (n, s) in memo:
    return memo[(n, s)]
  res = 0
  for i in range(n-1):
    res += dp(n-2, s[1:i+1] + d[s[:2]] + s[i+2:])
  memo[(n, s)] = res
  return res

print(dp(n, 'a'))

