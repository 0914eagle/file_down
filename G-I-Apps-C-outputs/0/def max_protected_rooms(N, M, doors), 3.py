
def max_protected_rooms(N, M, doors):
    graph = {}
    for u, v in doors:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)

    max_protected = 0
    for u, v in doors:
        if u == -1:
            start = v
        elif v == -1:
            start = u
        visited = set()
        queue = [start]
        protected = 0

        while queue:
            curr = queue.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            protected += 1
            for neighbor in graph[curr]:
                if (curr, neighbor) != (u, v) and (neighbor, curr) != (u, v) and neighbor not in visited:
                    queue.append(neighbor)

        max_protected = max(max_protected, protected)

    return max_protected

# Sample Input
N = 2
M = 3
doors = [(-1, 0), (-1, 1), (0, 1)]
print(max_protected_rooms(N, M, doors))
```
