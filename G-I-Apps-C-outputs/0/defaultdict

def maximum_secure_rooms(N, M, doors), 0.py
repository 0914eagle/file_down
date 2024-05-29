
from collections import defaultdict

def maximum_secure_rooms(N, M, doors):
    connections = defaultdict(set)
    for door in doors:
        u, v = door
        if u == -1 or v == -1:
            continue
        connections[u].add(v)
        connections[v].add(u)

    max_rooms = 0
    for key in connections:
        if -1 not in connections[key]:
            num_rooms = 1 + len(connections[key])
            max_rooms = max(max_rooms, num_rooms)

    return max_rooms

# Sample Input
N = 2
M = 3
doors = [(-1, 0), (-1, 1), (0, 1)]

print(maximum_secure_rooms(N, M, doors))
```
