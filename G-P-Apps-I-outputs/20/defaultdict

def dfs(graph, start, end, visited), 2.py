
from collections import defaultdict

def dfs(graph, start, end, visited):
    if start == end:
        return True
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, end, visited):
                return True
    return False

def min_time_to_cross_river(P, R, L, logs):
    graph = defaultdict(list)
    for log in logs:
        graph[log[0]].append(log[1])
        graph[log[1]].append(log[0])

    visited = [False] * (R + 2)
    if not dfs(graph, -2, -1, visited):
        return P

    time = 0
    for _ in range(P):
        time += 1
        for log in logs:
            if log[0] == -2:
                logs.remove(log)
                break
        if not dfs(graph, -2, -1, visited):
            return P
    return time

# Input parsing
P, R, L = map(int, input().split())
logs = []
for _ in range(L):
    E1, E2 = map(int, input().split())
    logs.append((E1, E2))

# Call the function and print the result
result = min_time_to_cross_river(P, R, L, logs)
print(result)
```
