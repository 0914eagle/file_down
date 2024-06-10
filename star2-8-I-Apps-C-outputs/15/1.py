
n = int(input())
a = list(map(int, input().split()))

if 0 not in a:
    print(-1)
else:
    g = max(a)
    for i in range(n):
        g = min(g, a[i] * n // (n - i))
    print(sum(g - a[i] for i in range(n)))

