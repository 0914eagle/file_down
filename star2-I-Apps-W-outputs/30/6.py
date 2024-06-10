
A, B, n, x = map(int, input().split())
def f(x):
    return A * x + B
def g(n, x):
    if n == 0:
        return x
    return f(g(n - 1, x))
print(g(n, x) % (10**9 + 7))

