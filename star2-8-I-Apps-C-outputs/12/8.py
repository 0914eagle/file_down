
def solve(n, m):
  if n > m:
    n, m = m, n
  return 4 * (n // 2) * (m // 2)

