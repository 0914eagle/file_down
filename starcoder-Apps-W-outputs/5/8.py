
import sys

def dfs(node):
    global visited
    visited[node] = True
    for i in g[node]:
        if not visited[i]:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())

g = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

visited = [False]*(n+1)

dfs(1)

ans = []
for i in range(2, n+1):
    if not visited[i]:
        ans.append(i)
if len(ans) == 0:
    print("Connected")
else:
    for i in ans:
        print(i)
