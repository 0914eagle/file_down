
MOD = 10**9 + 7

def dfs(node, parent, graph, white_dist, black_dist):
    white_max = 0
    black_max = 0
    for child in graph[node]:
        if child != parent:
            white_child, black_child = dfs(child, node, graph, white_dist, black_dist)
            white_max = max(white_max, white_child + 1)
            black_max = max(black_max, black_child + 1)
    
    white_dist[node] = white_max
    black_dist[node] = black_max
    
    return white_max, black_max

def sum_niceness(N, edges):
    graph = {i: [] for i in range(1, N+1)}
    white_dist = [0] * (N+1)
    black_dist = [0] * (N+1)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    dfs(1, 0, graph, white_dist, black_dist)
    
    total_niceness = 0
    for i in range(1, N+1):
        total_niceness = (total_niceness + max(white_dist[i], black_dist[i])) % MOD
    
    return total_niceness

# Sample Input
N = 2
edges = [(1, 2)]

result = sum_niceness(N, edges)
print(result)
```
