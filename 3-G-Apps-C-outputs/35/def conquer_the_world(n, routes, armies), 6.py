
import heapq

def conquer_the_world(n, routes, armies):
    graph = [[] for _ in range(n)]
    for u, v, c in routes:
        graph[u-1].append((v-1, c))
        graph[v-1].append((u-1, c))
    
    total_cost = 0
    total_armies = sum(armies)
    remaining_armies = list(armies)
    visited = [False] * n
    pq = [(0, 0)]  # (cost, node)
    
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost
        
        for neighbor, neighbor_cost in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (neighbor_cost, neighbor))
                remaining_armies[neighbor] = max(remaining_armies[neighbor], armies[neighbor])
    
    return total_cost

# Input parsing
n = int(input())
routes = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    routes.append((u, v, c))
armies = []
for _ in range(n):
    x, y = map(int, input().split())
    armies.append(y)

# Call the function and print the result
print(conquer_the_world(n, routes, armies))
