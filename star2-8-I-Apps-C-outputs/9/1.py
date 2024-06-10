
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(adj_list, start, end):
    dist = defaultdict(lambda: float('inf'))
    visited = set()
    pq = []
    
    dist[start] = 0
    heappush(pq, (0, start))
    
    while pq:
        curr_dist, curr_node = heappop(pq)
        
        if curr_node == end:
            return curr_dist
        
        if curr_node in visited:
            continue
        
        visited.add(curr_node)
        
        for neighbor, weight in adj_list[curr_node]:
            if neighbor in visited:
                continue
            
            new_dist = curr_dist | weight
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))
    
    return -1
    
n, m = map(int, input().split())
adj_list = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))
    
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    print(dijkstra(adj_list, s, t))

