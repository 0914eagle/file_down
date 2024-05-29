
def make_tourist_friendly(N, E, roads):
    graph = [[] for _ in range(N)]
    in_degree = [0] * N
    out_degree = [0] * N
    
    for a, b in roads:
        graph[a - 1].append(b - 1)
        in_degree[b - 1] += 1
        out_degree[a - 1] += 1
    
    start_city = None
    end_city = None
    
    for i in range(N):
        if in_degree[i] == out_degree[i] + 1:
            if end_city is not None:
                return "NO"
            end_city = i
        elif in_degree[i] + 1 == out_degree[i]:
            if start_city is not None:
                return "NO"
            start_city = i
        elif in_degree[i] != out_degree[i]:
            return "NO"
    
    if end_city is None and start_city is None:
        start_city = roads[0][0] - 1
    
    stack = []
    path = []
    if start_city is not None:
        stack.append(start_city)
    
    while stack:
        u = stack[-1]
        if not graph[u]:
            path.append(u)
            stack.pop()
        else:
            v = graph[u].pop()
            stack.append(v)
    
    if len(path) != E + 1 or path[0] != path[-1]:
        return "NO"
    
    path = path[::-1]
    
    result = "YES\n"
    for i in range(len(path) - 1):
        result += f"{path[i] + 1} {path[i + 1] + 1}\n"
    
    return result

# Input parsing
N, E = map(int, input().split())
roads = []
for _ in range(E):
    a, b = map(int, input().split())
    roads.append((a, b))

# Function call and output
print(make_tourist_friendly(N, E, roads))
```
