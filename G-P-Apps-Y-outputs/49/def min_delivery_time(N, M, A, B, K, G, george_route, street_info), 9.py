
def min_delivery_time(N, M, A, B, K, G, george_route, street_info):
    INF = float('inf')
    
    # Build graph
    graph = {i: {} for i in range(1, N+1)}
    for a, b, l in street_info:
        graph[a][b] = l
        graph[b][a] = l
    
    # Create a list to store the time each intersection is blocked by Mister George
    blocked_time = [0] * (N+1)
    for i in range(len(george_route)-1):
        start_time = i * 5
        end_time = start_time + graph[george_route[i]][george_route[i+1]]
        for j in range(start_time, end_time):
            blocked_time[george_route[i]] = max(blocked_time[george_route[i]], j)
    
    # Apply Dijkstra's algorithm to find the shortest path from A to B
    dist = [INF] * (N+1)
    dist[A] = K
    visited = set()
    while len(visited) < N:
        u = min((v for v in range(1, N+1) if v not in visited), key=lambda x: dist[x])
        visited.add(u)
        for v in graph[u]:
            if blocked_time[u] < dist[u] < blocked_time[u] + 5:  # Wait until the street is no longer blocked
                dist[u] = blocked_time[u] + 5
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    
    return dist[B]

# Read input
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
george_route = list(map(int, input().split()))
street_info = [list(map(int, input().split())) for _ in range(M)]

# Calculate and print the result
result = min_delivery_time(N, M, A, B, K, G, george_route, street_info)
print(result)
```
