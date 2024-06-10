
h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
mod = 10**9 + 7

def fact(n):
  res = 1
  for i in range(1, n+1):
    res *= i
  return res

def C(n, r):
  return fact(n) // (fact(r) * fact(n-r))

ways = 1
for i in range(h):
  ways *= C(r[i] + c[i], r[i])
  ways %= mod
print(ways % mod)

