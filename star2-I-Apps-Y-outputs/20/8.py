
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

def f(x):
    return (100 + p * (x - 1)) / 100 * t[x - 1]

def g(x):
    return (100 + p * x) / 100 * t[x]

def h(x):
    return (100 + p * x) / 100 * k

ans = 0
for i in range(1, n + 1):
    ans += f(i) - g(i - 1)
ans += h(n) - g(n)
print(ans)

