
from collections import defaultdict
import heapq

def dijkstra(graph, src, dst):
  visited = set()
  distances = defaultdict(lambda: float('inf'))
  distances[src] = 0
  prev_nodes = defaultdict(lambda: None)
  heap = [(0, src)]

  while heap:
    curr_dist, curr_node = heapq.heappop(heap)
    
    if curr_node == dst:
      break
    
    if curr_node in visited:
      continue
    
    visited.add(curr_node)
    
    for neighbor, weight in graph[curr_node]:
      if neighbor not in visited:
        if distances[neighbor] > distances[curr_node] + weight:
          distances[neighbor] = distances[curr_node] + weight
          prev_nodes[neighbor] = curr_node
          heapq.heappush(heap, (distances[neighbor], neighbor))

  path = []
  curr_node = dst

  while curr_node is not None:
    path.append(curr_node)
    curr_node = prev_nodes[curr_node]

  return distances[dst], path[::-1]

def main():
  n, r = list(map(int, input().split()))
  flights = []
  graph = defaultdict(list)

  for _ in range(r):
    a, b, c = list(map(int, input().split()))
    flights.append((a, b, c))
    flights.append((b, a, c))

  for a, b, c in flights:
    graph[a].append((b, c))

  f = int(input())
  flights = []

  for _ in range(f):
    a, b, c = list(map(int, input().split()))
    flights.append((a, b, c))
    flights.append((b, a, c))

  for a, b, c in flights:
    graph[a].append((b, c))

  min_cost, path = dijkstra(graph, 1, 1)

  print(min_cost)

if __name__ == '__main__':
  main()

