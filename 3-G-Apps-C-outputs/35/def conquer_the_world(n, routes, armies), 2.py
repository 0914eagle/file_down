
import heapq

def conquer_the_world(n, routes, armies):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, c in routes:
        graph[u].append((v, c))
        graph[v].append((u, c))
    
    min_cost = 0
    heap = [(0, 1)]
    visited = set()
    while heap:
        cost, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        min_cost += cost
        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (neighbor_cost, neighbor))
    
    total_armies = sum(armies)
    return min_cost * total_armies

# Input parsing
n = int(input())
routes = [list(map(int, input().split())) for _ in range(n-1)]
armies = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
print(conquer_the_world(n, routes, armies))
