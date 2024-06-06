
def dfs(v, p=-1):
    global c
    for u in g[v]:
        if u != p:
            c[v] += c[u]
            dfs(u, v)

n, m = map(int, input().split())
r = list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
for _ in range(m):
    x = list(map(int, input().split()))
    for i in range(x[0] - 1):
        for j in range(i + 1, x[0]):
            g[x[i + 1]].append(x[j + 1])
            g[x[j + 1]].append(x[i + 1])

c = r[:]
dfs(1)
print('YES' if c.count(0) else 'NO')
