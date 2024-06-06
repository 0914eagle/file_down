
for _ in range(int(input())):
    s, b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d, g = [], []
    for i in range(b):
        x, y = map(int, input().split())
        d.append(x)
        g.append(y)
    d.sort()
    p, j, ans = 0, 0, [0 for _ in range(s)]
    for i in range(s):
        while p < b and d[p] <= a[i]:
            p += 1
        ans[i] = sum(g[:p])
        for j in range(j, p):
            g[j] = 0
    print(*ans)
