
def make_tourist_friendly(N, E, roads):
    graph = {}
    for a, b in roads:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    
    out_degrees = [0] * (N + 1)
    in_degrees = [0] * (N + 1)
    for a in graph:
        out_degrees[a] = len(graph[a])
        for b in graph[a]:
            in_degrees[b] += 1
    
    for a in graph.keys():
        if out_degrees[a] != in_degrees[a]:
            return "NO"
    
    visited = [False] * (N + 1)
    tour = []
    
    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        tour.append(node)
    
    for node in graph:
        if not visited[node]:
            dfs(node)
    
    if len(tour) != E + 1:
        return "NO"
    else:
        return "YES\n" + "\n".join(f"{tour[i]} {tour[i+1]}" for i in range(E))

# Input handling
N, E = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(E)]

# Call the function and print the result
result = make_tourist_friendly(N, E, roads)
print(result)
```
