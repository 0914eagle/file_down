
import sys
from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.V = vertices # No. of vertices
    self.graph = defaultdict(list) # default dictionary to store graph
  def add_edge(self, u, v, w):
    self.graph[u].append((v, w))
  def Dijkstra(self, src, dest):
    dist = [sys.maxsize] * self.V
    dist[src] = 0
    sptSet = [False] * self.V
    for _ in range(self.V):
      u = self.min_dist(dist, sptSet)
      sptSet[u] = True
      for v, w in self.graph[u]:
        if sptSet[v] == False and dist[u] != sys.maxsize and dist[u]+w < dist[v]:
          dist[v] = dist[u] + w
    return dist[dest]
  def min_dist(self, dist, sptSet):
    min_val = sys.maxsize
    min_index = -1
    for v in range(self.V):
      if dist[v] < min_val and sptSet[v] == False:
        min_val = dist[v]
        min_index = v
    return min_index

def main():
  v, e = map(int, input().split())
  graph = Graph(v)
  for _ in range(e):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)
  s, t = map(int, input().split())
  dist = graph.Dijkstra(s, t)
  cnt = 0
  for u in graph.graph:
    for v, _ in graph.graph[u]:
      if graph.Dijkstra(u, v) + graph.Dijkstra(v, t) == dist:
        cnt += 1
  print(cnt)

if __name__ == "__main__":
  main()

