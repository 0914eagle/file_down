
import heapq
import sys

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = [[] for _ in range(num_nodes)]

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start):
        dist = [float('inf')] * self.num_nodes
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, weight in self.adj_list[u]:
                new_dist = dist[u] | weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return dist

def solve_transportation_cost(n, m, roads, q, queries):
    magical_island = Graph(n)
    for a, b, w in roads:
        magical_island.add_edge(a-1, b-1, w)

    distances = magical_island.dijkstra(0)
    
    result = []
    for s, t in queries:
        result.append(distances[s-1] | distances[t-1])

    return result

# Input parsing
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

# Solve and output
result = solve_transportation_cost(n, m, roads, q, queries)
for res in result:
    print(res)
```
