
n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ans = [0] * n
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(n):
        if a[j][y] == 1 and j != x:
            ans[j] += 1
print(*ans)
