
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

def f(x):
    return (100 + p * (x - 1)) / 100

def g(x):
    return x * f(x)

def h(x):
    return g(x) - x

def calc(l, r, x):
    return h(r) - h(l) - (r - l) * x

def solve(l, r):
    if abs(r - l) < 1e-6:
        return l
    m = (l + r) / 2
    if calc(l, m, f(l)) > calc(m, r, f(r)):
        return solve(l, m)
    else:
        return solve(m, r)

print(solve(0, k))

