
def dfs(v, p, d):
    global res, a, b, c
    if d > res:
        res = d
        a, b, c = p, v, v
    for u in g[v]:
        if u != p:
            dfs(u, v, d + 1)


n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

res = 0
a, b, c = 0, 0, 0
dfs(0, 0, 0)
dfs(a, a, 0)
dfs(b, b, 0)
print(res)
print(a + 1, b + 1, c + 1)

