
from collections import defaultdict

def max_secure_rooms(N, M, doors):
    adj_list = defaultdict(list)
    for door in doors:
        u, v = door
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def dfs(node, visited):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    
    max_rooms = 0
    for room in range(N):
        visited = set()
        dfs(room, visited)
        num_rooms = len(visited)
        if num_rooms > max_rooms:
            max_rooms = num_rooms
    
    return max_rooms - 1  # Exclude the room we are starting from

# Sample Input
N = 2
M = 3
doors = [
    [-1, 0],
    [-1, 1],
    [0, 1]
]

# Sample Output
print(max_secure_rooms(N, M, doors))
```
