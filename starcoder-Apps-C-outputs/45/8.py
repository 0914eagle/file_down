
n, r, p = map(int, input().split())

ans = n * p
for i in range(n + 1):
    ans = min(ans, r + i * p)

print(ans)
