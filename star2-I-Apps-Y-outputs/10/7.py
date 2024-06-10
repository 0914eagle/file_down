
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def f(x, y):
    return a*x + b*y

def g(x, y):
    return 2*x + y

def h(x, y):
    return x + y

def is_valid(x, y):
    return x >= 1 and y >= 1 and g(x, y) >= sigma and h(x, y) <= m

def solve(x, y):
    if is_valid(x, y):
        return f(x, y)
    if x == 1:
        return solve(x, y-1)
    if y == 1:
        return solve(x-1, y)
    return max(solve(x-1, y), solve(x, y-1))

print(solve(m//2, m//2))

