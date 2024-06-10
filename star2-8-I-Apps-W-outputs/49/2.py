
n, k = map(int, input().split())
h = list(map(int, input().split()))
mod = 998244353

def solve(n, k, h):
  if n == 1:
    return k - 1
  if n == 2:
    return (k - 1)**2
  if n == 3:
    return ((k - 1)**3 + (k - 1)**2 + (k - 1)) % mod
  dp = [[0] * k for _ in range(n)]
  for i in range(k):
    dp[0][i] = 1
  for i in range(1, n):
    for j in range(k):
      for x in range(k):
        if j != h[i - 1] or x != h[i]:
          dp[i][j] += dp[i - 1][x]
          dp[i][j] %= mod
  return sum(dp[n - 1]) % mod

print(solve(n, k, h))

