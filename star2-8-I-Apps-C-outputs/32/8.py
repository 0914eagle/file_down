
from collections import defaultdict
import heapq

def dijkstra(graph, src):
    heap = []
    heapq.heappush(heap, (0, src))
    dist = defaultdict(lambda: float('inf'))
    dist[src] = 0
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dist[cur_node]:
            continue
            
        for neighbor, weight in graph[cur_node]:
            if dist[neighbor] > cur_dist + weight:
                dist[neighbor] = cur_dist + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
                
    return dist
    
def solve(n, r, flights, f, additional_flights):
    graph = defaultdict(list)
    
    for a, b, c in flights:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    for a, b, c in additional_flights:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    dist = dijkstra(graph, 1)
    
    total_cost = 0
    
    for a, b, c in flights:
        total_cost += dist[a] + dist[b]
        
    return total_cost
    
n, r = map(int, input().split())
flights = []

for _ in range(r):
    a, b, c = map(int, input().split())
    flights.append((a, b, c))
    
f = int(input())
additional_flights = []

for _ in range(f):
    a, b, c = map(int, input().split())
    additional_flights.append((a, b, c))
    
print(solve(n, r, flights, f, additional_flights))

