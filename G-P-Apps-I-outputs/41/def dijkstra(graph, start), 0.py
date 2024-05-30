
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance | weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def solve(n, m, roads, q, queries):
    graph = {i: {} for i in range(1, n+1)}
    
    for a, b, w in roads:
        if b in graph[a]:
            graph[a][b] = graph[a][b] | w
            graph[b][a] = graph[a][b]
        else:
            graph[a][b] = w
            graph[b][a] = w
    
    for s, t in queries:
        distances = dijkstra(graph, s)
        print(distances[t])

# Input parsing
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Solve the problem
solve(n, m, roads, q, queries)
```
