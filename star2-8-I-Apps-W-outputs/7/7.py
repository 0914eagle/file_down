

class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = []

  def addEdge(self, u, v, w):
    self.graph.append([u, v, w])

  def BFS(self, s, t):
    visited = [False] * self.V
    queue = []
    queue.append(s)
    visited[s] = True
    parent = [-1] * self.V
    while queue:
      u = queue.pop(0)
      for i in self.graph:
        if i[0] == u and not visited[i[1]]:
          visited[i[1]] = True
          queue.append(i[1])
          parent[i[1]] = u
    path = []
    temp = t
    while temp != -1:
      path.append(temp)
      temp = parent[temp]
    if s not in path:
      return 0
    return len(path) - 1

V, E = map(int, input().split())
graph = Graph(V)
for i in range(E):
  u, v, w = map(int, input().split())
  graph.addEdge(u, v, w)
s, t = map(int, input().split())
print(graph.BFS(s, t))


