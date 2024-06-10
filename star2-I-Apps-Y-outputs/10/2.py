
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def f(x, y):
  return a*x + b*y

def g(x, y):
  return 2*x + y

def h(x, y):
  return x + y

def solve(x, y):
  if x == 0 or y == 0:
    return 0
  if g(x, y) >= sigma and h(x, y) <= m:
    return max(f(x, y), solve(x-1, y), solve(x, y-1))
  else:
    return max(solve(x-1, y), solve(x, y-1))

print(solve(m//2, m//2))

