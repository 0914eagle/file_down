
import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
def solve():
  n, m = map(int, input().split())
  s1 = list(map(int, input().split()))
  s2 = list(map(int, input().split()))
  count = 0
  for i in range(n):
    if s1[i] == 0 and s2[i] == 0:
      count += 1
    elif s1[i] == 0 or s2[i] == 0:
      continue
    elif s1[i] > s2[i]:
      count = 0
      break
  if count == 0:
    return 0
  mod = 10**9 + 7
  q = (m - 1)**count
  p = m**(count - 1)
  for i in range(1, count + 1):
    p = (p * (m - 1)) % mod
  inv = pow(q, mod - 2, mod)
  res = (p * inv) % mod
  return res
print(solve())

