
n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

def dfs(v, p):
    global g, d, res
    d[v] = d[p] + 1
    for u in g[v]:
        if u != p:
            dfs(u, v)
    res = max(res, d[v])

d = [0] * n
res = 0
dfs(0, -1)

def dfs2(v, p):
    global g, d, res, ans
    d[v] = d[p] + 1
    if d[v] == res:
        ans = v
    for u in g[v]:
        if u != p:
            dfs2(u, v)

d = [0] * n
ans = 0
dfs2(0, -1)

def dfs3(v, p):
    global g, d, res, ans, a
    d[v] = d[p] + 1
    if d[v] == res:
        a = v
    for u in g[v]:
        if u != p:
            dfs3(u, v)

d = [0] * n
a = 0
dfs3(ans, -1)

print(res)
print(ans + 1, a + 1, 1)

