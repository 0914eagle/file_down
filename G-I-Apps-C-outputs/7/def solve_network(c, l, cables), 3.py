
def solve_network(c, l, cables):
    graph = {i: set() for i in range(c)}
    for cable in cables:
        a, b = cable
        graph[a].add(b)
        graph[b].add(a)

    max_hops = 0
    for i in range(c):
        visited = [False] * c
        hops = 0
        stack = [(i, 0)]
        while stack:
            node, depth = stack.pop()
            visited[node] = True
            hops = max(hops, depth)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append((neighbor, depth + 1))
        max_hops = max(max_hops, hops)

    return max_hops

# Sample Input
computers = 6
existing_cables = 4
existing_cables_info = [(0, 1), (0, 2), (3, 4), (3, 5)]

print(solve_network(computers, existing_cables, existing_cables_info))  # Output: 3
```
