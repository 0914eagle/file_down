
def build_network(nodes, cables):
    graph = {i: [] for i in range(nodes)}
    
    for a, b in cables:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * nodes
    max_hops = 0
    
    def dfs(node, depth):
        nonlocal max_hops
        visited[node] = True
        max_hops = max(max_hops, depth)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, depth + 1)
    
    for node in range(nodes):
        if not visited[node]:
            dfs(node, 0)
    
    return max_hops

# Reading input
c, l = map(int, input().split())
existing_cables = [tuple(map(int, input().split())) for _ in range(l)]

# Calling the function
result = build_network(c, existing_cables)
print(result)
```
