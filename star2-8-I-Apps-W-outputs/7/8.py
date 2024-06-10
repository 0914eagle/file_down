
import sys
import math

def dijkstra(graph, src, dest):
  shortest_dist = [math.inf] * len(graph)
  shortest_dist[src] = 0
  visited = [False] * len(graph)
  prev = [None] * len(graph)

  while True:
    min_dist = math.inf
    min_node = None
    for i in range(len(graph)):
      if not visited[i] and shortest_dist[i] < min_dist:
        min_dist = shortest_dist[i]
        min_node = i

    if min_node is None:
      break

    visited[min_node] = True
    for neighbour, weight in graph[min_node]:
      if not visited[neighbour] and shortest_dist[neighbour] > shortest_dist[min_node] + weight:
        shortest_dist[neighbour] = shortest_dist[min_node] + weight
        prev[neighbour] = min_node

  paths = []
  curr = dest
  while curr is not None:
    paths.append(curr)
    curr = prev[curr]

  return paths

def main():
  V, E = map(int, input().split())
  graph = [[] for _ in range(V)]
  for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
  s, t = map(int, input().split())
  paths = dijkstra(graph, s, t)
  num_paths = len(paths)
  print(num_paths)

if __name__ == "__main__":
  main()

