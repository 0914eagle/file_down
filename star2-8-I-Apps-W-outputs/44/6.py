
n, m = map(int, input().split())
p = list(map(int, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    p[a], p[b] = p[b], p[a]
print(*sorted(p, reverse=True))

