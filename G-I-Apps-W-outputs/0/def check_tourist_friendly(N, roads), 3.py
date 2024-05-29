
def check_tourist_friendly(N, roads):
    graph = {}
    in_degrees = [0] * (N + 1)
    out_edges = {}
    
    for a, b in roads:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        
        in_degrees[b] += 1
        
        if a not in out_edges:
            out_edges[a] = b
        else:
            return "NO"
    
    start = None
    end = None
    for i in range(1, N + 1):
        if in_degrees[i] == 0:
            if start is not None:
                return "NO"
            start = i
        elif in_degrees[i] != 1:
            return "NO"
    
    if start is None:
        return "NO"
    
    path = []
    curr = start
    while len(path) < len(roads):
        path.append(curr)
        if curr in out_edges:
            next_city = out_edges[curr]
            del out_edges[curr]
            curr = next_city
        else:
            return "NO"
    
    if curr != start:
        return "NO"
    
    result = ["YES"]
    for city in path:
        result.append(f"{city} {out_edges[city]}")
    
    return "\n".join(result)

# Input processing
N, E = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(E)]

# Call the function and print the output
print(check_tourist_friendly(N, roads))
```
