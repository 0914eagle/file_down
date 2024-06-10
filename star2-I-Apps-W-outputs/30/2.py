
def f(x, A, B):
    return (A * x + B) % (10**9 + 7)


def g(x, A, B, n):
    if n == 0:
        return x
    else:
        return f(g(x, A, B, n - 1), A, B)


A, B, n, x = map(int, input().split())
print(g(x, A, B, n))

