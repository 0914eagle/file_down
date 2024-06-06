
n, m = list(map(int, input().split()))
c = []
for i in range(m):
    c.append(list(map(int, input().split())))
t = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    x1, y1, x2, y2 = c[i][0], c[i][1], c[i][2], c[i][3]
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            t[i][j] = 1
for i in range(n+1):
    if t[1][i] == 1:
        t[1][i] = 0
    else:
        t[1][i] = 1
for i in range(2, n+1):
    for j in range(n+1):
        if t[i-1][j] == 1 and t[i][j] == 1:
            t[i][j] = 0
        else:
            t[i][j] = 1
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if t[i][j] == 0:
            ans += min(i, j)
print(ans)
