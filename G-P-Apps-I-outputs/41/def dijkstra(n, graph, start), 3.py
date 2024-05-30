
import heapq

def dijkstra(n, graph, start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if dist > distance[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist | weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distance

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

q = int(input())

distances = dijkstra(n, graph, 1)

for _ in range(q):
    s, t = map(int, input().split())
    print(distances[s] ^ distances[t])
