
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: x[0])
ans = 0
for i in range(n):
    if a[i][0] - a[i-1][0] - a[i-1][1] >= m:
        ans += 1
print(ans)
