
from collections import deque
def bfs(graph, start):
  visited = set()
  queue = deque([start])
  while queue:
    vertex = queue.popleft()
    if vertex not in visited:
      visited.add(vertex)
      queue.extend(graph[vertex] - visited)
  return visited
def solve(n, edges):
  graph = {i: set() for i in range(1, n+1)}
  for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)
  max_ind_set = 0
  for v in range(1, n+1):
    if len(bfs(graph, v)) == n:
      max_ind_set = max(max_ind_set, 1)
  return max_ind_set

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, edges))

