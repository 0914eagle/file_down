

def dfs(u):
    global vis, m, ch, cnt
    vis[u] = 1
    ch[u] = cnt
    for v in g[u]:
        if not vis[v]:
            dfs(v)
    return


n = int(input())
l = int(input())
w = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(n):
    adj = list(map(int, input().split()))
    for j in adj[1:]:
        g[i].append(j)
vis = [0 for i in range(n)]
ch = [0 for i in range(n)]
for i in range(n):
    if not vis[i]:
        cnt = i
        dfs(i)

ans = 1
for i in range(l):
    ans *= 1 - 2 ** (-ch[w[i]] - 1)
print(ans)


