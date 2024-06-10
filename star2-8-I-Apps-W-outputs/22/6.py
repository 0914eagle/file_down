
n = int(input())
a = list(map(int, input().split()))
adj = [[] for _ in range(n)]
for i in range(n):
    adj[i].append(a[i] - 1)

def dfs(u, parent):
    vis[u] = True
    for v in adj[u]:
        if not vis[v]:
            dfs(v, u)
        else:
            if v != parent:
                cycle.append(u)
                v = parent
                while v != u:
                    cycle.append(v)
                    v = parent[v]
                cycle.append(u)
    return

def solve():
    res = 1
    for i in range(n):
        if not vis[i]:
            cycle = []
            dfs(i, -1)
            if len(cycle) == 0:
                res = (res * 2) % (10**9 + 7)
            else:
                res = (res * (2**(len(cycle) - 1))) % (10**9 + 7)
    return res

vis = [False for _ in range(n)]
res = solve()
print(res)

