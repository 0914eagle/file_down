
n, m = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
def dfs(x, f):
    vis[x] = 1
    for i in edge[x]:
        if not vis[i]:
            dfs(i, f)
    f.append(x)
def find_is(x, f):
    vis[x] = 1
    for i in edge[x]:
        if not vis[i]:
            find_is(i, f)
vis = [0 for i in range(n)]
f = []
for i in range(n):
    if not vis[i]:
        dfs(i, f)
f.reverse()
vis = [0 for i in range(n)]
cnt = 0
for i in f:
    if not vis[i]:
        find_is(i, [])
        cnt += 1
print(n - cnt)

