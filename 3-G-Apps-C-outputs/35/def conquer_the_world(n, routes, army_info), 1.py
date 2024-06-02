
import heapq

def conquer_the_world(n, routes, army_info):
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
        total_cost += cost
        
        for neighbor, c in graph[node]:
            new_cost = cost + c
            if new_cost < min_cost[neighbor]:
                heapq.heappush(heap, (new_cost, neighbor))
    
    result = 0
    for i in range(n):
        result += max(0, army_info[i][1] - army_info[i][0]) * min_cost[i]
    
    return result

# Input
n = int(input())
routes = [list(map(int, input().split())) for _ in range(n-1)]
army_info = [list(map(int, input().split())) for _ in range(n)]

# Output
print(conquer_the_world(n, routes, army_info))
