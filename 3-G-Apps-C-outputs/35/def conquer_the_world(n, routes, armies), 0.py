
import heapq

def conquer_the_world(n, routes, armies):
    graph = {}
    for u, v, c in routes:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = c
        graph[v][u] = c

    total_cost = 0
    pq = []
    for i in range(1, n+1):
        if armies[i-1][0] < armies[i-1][1]:
            heapq.heappush(pq, (0, i))

    while pq:
        cost, node = heapq.heappop(pq)
        if armies[node-1][0] >= armies[node-1][1]:
            continue
        total_cost += cost
        armies[node-1][0] += 1
        for neighbor, neighbor_cost in graph[node].items():
            if armies[neighbor-1][0] < armies[neighbor-1][1]:
                heapq.heappush(pq, (neighbor_cost, neighbor))

    return total_cost

# Input
n = int(input())
routes = [list(map(int, input().split())) for _ in range(n-1)]
armies = [list(map(int, input().split())) for _ in range(n)]

# Output
print(conquer_the_world(n, routes, armies))
