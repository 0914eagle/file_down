
import heapq

def conquer_the_world(n, routes, armies):
    graph = [[] for _ in range(n)]
    for u, v, c in routes:
        graph[u-1].append((v-1, c))
        graph[v-1].append((u-1, c))
    
    total_cost = 0
    min_cost = [float('inf')] * n
    heap = [(0, 0)]  # (cost, node)
    
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > min_cost[node]:
            continue
        
        min_cost[node] = cost
        total_cost += cost * armies[node][1]
        
        for neighbor, neighbor_cost in graph[node]:
            new_cost = cost + neighbor_cost
            if new_cost < min_cost[neighbor]:
                heapq.heappush(heap, (new_cost, neighbor))
    
    return total_cost

# Input parsing
n = int(input())
routes = [list(map(int, input().split())) for _ in range(n-1)]
armies = [list(map(int, input().split())) for _ in range(n)]

result = conquer_the_world(n, routes, armies)
print(result)
