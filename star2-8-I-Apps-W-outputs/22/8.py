
n = int(input())
a = list(map(int, input().split()))

def flip(n, a):
  graph = [[] for i in range(n)]
  for i in range(n):
    graph[i].append(a[i] - 1)
  visited = [0 for i in range(n)]
  def dfs(u, path):
    if visited[u] == 1:
      if u in path:
        return path[path.index(u):]
      else:
        return []
    visited[u] = 1
    path.append(u)
    for v in graph[u]:
      res = dfs(v, path)
      if len(res) > 0:
        return res
    path.pop()
    return []
  cycles = []
  for i in range(n):
    if visited[i] == 0:
      cycles.append(dfs(i, []))
  res = 1
  for cycle in cycles:
    res *= 2
    res %= (10**9 + 7)
  return res
print(flip(n, a))

