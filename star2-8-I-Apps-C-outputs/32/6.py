
def dijkstra(graph, start, end):
  distances = {vertex: float('inf') for vertex in graph}
  distances[start] = 0
  visited = set()
  vertices = list(graph)

  while vertices:
    current = min(vertices, key=lambda vertex: distances[vertex])
    vertices.remove(current)
    visited.add(current)
    for neighbour, weight in graph[current].items():
      if neighbour not in visited:
        distances[neighbour] = min(distances[neighbour], distances[current] + weight)

  return distances[end]

def solve(N, R, flights, F, additional_flights):
  graph = {airport: {} for airport in range(1, N+1)}
  for a, b, c in flights:
    graph[a][b] = c
    graph[b][a] = c
  for a, b, c in additional_flights:
    graph[a][b] = c
    graph[b][a] = c
  return dijkstra(graph, 1, 1)

if __name__ == '__main__':
  N, R = map(int, input().split())
  flights = [tuple(map(int, input().split())) for _ in range(R)]
  F = int(input())
  additional_flights = [tuple(map(int, input().split())) for _ in range(F)]
  print(solve(N, R, flights, F, additional_flights))

