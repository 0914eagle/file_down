
def find_waiting_time(n, m, trails):
    graph = {}
    for i in range(n):
        graph[i] = []
    
    for u, v, d in trails:
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    # Dijkstra's algorithm to find shortest path
    distances = [float('inf')] * n
    distances[0] = 0
    visited = [False] * n
    
    for _ in range(n):
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i
        
        visited[u] = True
        
        for v, d in graph[u]:
            if not visited[v] and distances[u] + d < distances[v]:
                distances[v] = distances[u] + d
    
    return distances[n-1] // 12

# Reading input
n, m = map(int, input().split())
trails = []
for _ in range(m):
    u, v, d = map(int, input().split())
    trails.append((u, v, d))

# Calling the function with input values and printing the result
print(find_waiting_time(n, m, trails))
```
