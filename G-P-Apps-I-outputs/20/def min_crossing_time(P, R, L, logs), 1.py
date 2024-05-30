
def min_crossing_time(P, R, L, logs):
    graph = {}
    for i in range(-2, R):
        graph[i] = []
    
    for log in logs:
        start, end = log
        graph[start].append(end)
        graph[end].append(start)
    
    visited = set()
    time = 0
    
    def dfs(node):
        nonlocal time
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                time += 1
                dfs(neighbor)
    
    dfs(-2)
    
    if len(visited) >= R + 1:
        return time * P
    else:
        return R + 1 - len(visited)

# Sample input
P, R, L = 2, 4, 7
logs = [(-2, 0), (0, -1), (-2, 1), (1, 0), (2, 1), (2, 3), (3, -1)]
print(min_crossing_time(P, R, L, logs))
