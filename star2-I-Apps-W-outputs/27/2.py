
def solve(n, b):
  b = [0] + b + [n - 1]
  res = [0] * n
  for i in range(n):
    res[i] = b[i] + 1
  return res

