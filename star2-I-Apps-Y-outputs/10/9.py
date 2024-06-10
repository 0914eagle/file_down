
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def f(x, y):
  return a*x + b*y

def g(x, y):
  return 2*x + y

def h(x, y):
  return x + y

def solve(f, g, h, m, sigma):
  x = sigma
  y = m - x
  while g(x, y) < sigma:
    x += 1
    y = m - x
  return f(x, y)

print(solve(f, g, h, m, sigma))

