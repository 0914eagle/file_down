
from collections import defaultdict

def minimum_crossing_time(P, R, L, logs):
    def dfs(current, target, visited):
        if current == target:
            return True
        
        visited[current] = True
        for neighbor in graph[current]:
            if not visited[neighbor] and dfs(neighbor, target, visited):
                return True
        return False

    graph = defaultdict(list)
    for log in logs:
        graph[log[0]].append(log[1])
        graph[log[1]].append(log[0])

    possible_crossings = 0
    for _ in range(P):
        visited = {b: False for b in range(-2, R)}
        if dfs(-2, -1, visited):
            possible_crossings += 1
    
    if possible_crossings < P:
        return P - possible_crossings
    else:
        return 2 * L + P

# Read input
P, R, L = map(int, input().split())
logs = [tuple(map(int, input().split())) for _ in range(L)]

# Call the function and print the result
print(minimum_crossing_time(P, R, L, logs))
```
