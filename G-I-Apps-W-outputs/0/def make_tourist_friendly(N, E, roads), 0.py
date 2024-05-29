
def make_tourist_friendly(N, E, roads):
    graph = {}
    in_degree = [0] * (N + 1)
    out_degree = [0] * (N + 1)
    for a, b in roads:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        out_degree[a] += 1
        in_degree[b] += 1
    
    euler_path = []
    def dfs(node):
        if node not in graph:
            return
        while graph[node]:
            neighbor = graph[node].pop()
            dfs(neighbor)
        euler_path.append(node)
    
    start_node = None
    for i in range(1, N + 1):
        if in_degree[i] != out_degree[i]:
            if in_degree[i] == out_degree[i] + 1:
                if start_node is not None:
                    return "NO"
                start_node = i
            elif out_degree[i] == in_degree[i] + 1:
                if start_node is not None:
                    return "NO"
                start_node = i
            else:
                return "NO"
    
    dfs(start_node)
    
    if len(euler_path) != E + 1:
        return "NO"
    
    result = []
    for i in range(len(euler_path) - 1):
        result.append((euler_path[i], euler_path[i + 1]))
    
    return "YES", result

# Example usage
N, E = 3, 3
roads = [(1, 2), (2, 3), (3, 1)]
output = make_tourist_friendly(N, E, roads)
if output == "NO":
    print("NO")
else:
    print("YES")
    for road in output[1]:
        print(road[0], road[1])
```
