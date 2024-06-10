
import sys
sys.setrecursionlimit(10**6)

def dfs(cur, parent, visited):
  visited[cur] = 1
  for child in adj[cur]:
    if child == parent:
      continue
    if visited[child]:
      return 1
    if dfs(child, cur, visited):
      return 1
  return 0

n, m = map(int, input().split())
adj = [[] for i in range(n)]
for i in range(m):
  u, v = map(int, input().split())
  adj[u].append(v)
  adj[v].append(u)

visited = [0] * n
if dfs(0, -1, visited):
  print("impossible")
else:
  print(n)

