
n, m = map(int, input().split())
p = list(map(int, input().split()))
pos = [0 for i in range(n + 1)]
for i in range(n):
    pos[p[i]] = i
for i in range(m):
    a, b = map(int, input().split())
    pos[p[a - 1]], pos[p[b - 1]] = pos[p[b - 1]], pos[p[a - 1]]
    p[a - 1], p[b - 1] = p[b - 1], p[a - 1]
print(' '.join(map(str, p)))

