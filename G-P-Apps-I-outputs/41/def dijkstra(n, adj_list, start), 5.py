
import heapq

def dijkstra(n, adj_list, start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
            continue
        for neighbor, weight in adj_list[node]:
            if dist | weight < distance[neighbor]:
                distance[neighbor] = dist | weight
                heapq.heappush(pq, (distance[neighbor], neighbor))

    return distance

def solve(n, m, roads, q, queries):
    adj_list = [[] for _ in range(n + 1)]
    for a, b, w in roads:
        adj_list[a].append((b, w))
        adj_list[b].append((a, w))

    distances = dijkstra(n, adj_list, 1)

    for s, t in queries:
        print(distances[s] ^ distances[t])

# Input parsing
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

# Solve the problem
solve(n, m, roads, q, queries)
```
