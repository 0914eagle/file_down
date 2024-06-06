
def ans(i):
    vis[i] = True
    for v in g[i]:
        if not vis[v]:
            ans(v)
    vis[i] = False
    res[0] = max(res[0], len(g[i]))

n = int(input())
g = [[] for i in range(n)]
res = [0]
for i in range(n):
    v, p = list(map(int, input().split()))
    if p != 0:
        g[p-1].append(i)
vis = [False]*n
ans(0)
print(res[0]+1)
