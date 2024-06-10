
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def f(x, y):
    return a*x + b*y

def g(x, y):
    return x + y - m

def h(x, y):
    return 2*x + y - sigma

def solve(a, b, c, d):
    x = max(0, -c/a)
    y = max(0, -d/b)
    while f(x, y) < f(x+1, y) and g(x+1, y) <= 0 and h(x+1, y) >= 0:
        x += 1
    while f(x, y) < f(x, y+1) and g(x, y+1) <= 0 and h(x, y+1) >= 0:
        y += 1
    return f(x, y)

print(solve(a, b, m, sigma))

