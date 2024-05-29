
def max_rooms_protected(N, M, doors):
    adj_list = {i: set() for i in range(N)}
    for door in doors:
        u, v = door
        adj_list[u].add(v)
        adj_list[v].add(u)

    visited = [False] * N

    def dfs(node):
        visited[node] = True
        count = 1
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                count += dfs(neighbor)
        return count

    max_rooms = 0
    for room in range(N):
        if not visited[room]:
            count = dfs(room)
            max_rooms = max(max_rooms, count)

    return max_rooms - 1

# Sample Input
N = 2
M = 3
doors = [(-1, 0), (-1, 1), (0, 1)]

print(max_rooms_protected(N, M, doors))
```
