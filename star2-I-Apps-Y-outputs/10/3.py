
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def R(x, y):
  return a*x + b*y

def solve(m, sigma):
  x = max(1, (sigma - m) // 2)
  y = m - x
  return R(x, y)

print(solve(m, sigma))

