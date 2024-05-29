
def max_secured_rooms(N, M, doors):
    graph = {i: set() for i in range(N)}
    for u, v in doors:
        if u != -1 and v != -1:
            graph[u].add(v)
            graph[v].add(u)
    
    visited = set()
    max_secured = 0

    def dfs(node):
        nonlocal max_secured
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        if -1 in graph[node]:
            max_secured += 1
        
    for room in range(N):
        if room not in visited:
            dfs(room)
    
    return max_secured

# Sample Input
N = 2
M = 3
doors = [(-1, 0), (-1, 1), (0, 1)]

print(max_secured_rooms(N, M, doors))  # Output: 0
```
