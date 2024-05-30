
from collections import defaultdict

def minimum_crossing_time(P, R, L, logs):
    connections = defaultdict(list)
    for i in range(L):
        E1, E2 = logs[i]
        connections[E1].append(E2)
        connections[E2].append(E1)

    visited = set()
    queue = [(0, 0)]  # (node, time)
    while queue:
        node, time = queue.pop(0)
        if node == -1:
            return time
        visited.add(node)
        for neighbor in connections[node]:
            if neighbor not in visited:
                queue.append((neighbor, time + 1))

    return P - len(visited)

# Input parsing
input_line = input().strip().split()
P = int(input_line[0])
R = int(input_line[1])
L = int(input_line[2])

logs = []
for _ in range(L):
    log_line = input().strip().split()
    E1, E2 = int(log_line[0]), int(log_line[1])
    logs.append((E1, E2))

# Call the function and print the result
result = minimum_crossing_time(P, R, L, logs)
print(result)
```
