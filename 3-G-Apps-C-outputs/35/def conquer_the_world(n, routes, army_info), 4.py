
import heapq

def conquer_the_world(n, routes, army_info):
    graph = [[] for _ in range(n)]
    for u, v, c in routes:
        graph[u-1].append((v-1, c))
        graph[v-1].append((u-1, c))
    
    min_cost = 0
    total_armies = sum(army_info)
    visited = [False] * n
    pq = [(0, 0)]  # (cost, node)
    
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        min_cost += cost
        
        for neighbor, c in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (c, neighbor))
    
    return min_cost

# Input processing
n = int(input())
routes = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    routes.append((u, v, c))
    
army_info = []
for _ in range(n):
    x, y = map(int, input().split())
    army_info.append(y)

result = conquer_the_world(n, routes, army_info)
print(result)
