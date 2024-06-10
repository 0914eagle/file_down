
class BeeHive:
  def __init__(self):
    self.adj_list = []
  def add_edge(self, u, v):
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)
  def bfs(self, start):
    visited = [False] * len(self.adj_list)
    queue = [start]
    visited[start] = True
    while queue:
      current = queue.pop(0)
      for neighbor in self.adj_list[current]:
        if not visited[neighbor]:
          visited[neighbor] = True
          queue.append(neighbor)
    return visited
  def solve(self):
    n, m = map(int, input().split())
    self.adj_list = [[] for _ in range(n)]
    for _ in range(m):
      u, v = map(int, input().split())
      self.add_edge(u, v)
    visited = self.bfs(0)
    if all(visited):
      print(n)
    else:
      print("impossible")
bee_hive = BeeHive()
bee_hive.solve()

