
n, m = map(int, input().split())
p = list(map(int, input().split()))
positions = [0] * (n + 1)
for i in range(n):
    positions[p[i]] = i
for _ in range(m):
    a, b = map(int, input().split())
    positions[p[a - 1]], positions[p[b - 1]] = positions[p[b - 1]], positions[p[a - 1]]
    p[a - 1], p[b - 1] = p[b - 1], p[a - 1]
print(*p)

