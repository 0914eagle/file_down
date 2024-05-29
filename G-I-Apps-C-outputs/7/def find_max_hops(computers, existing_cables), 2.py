
def find_max_hops(computers, existing_cables):
    graph = [[] for _ in range(computers)]
    for cable in existing_cables:
        graph[cable[0]].append(cable[1])
        graph[cable[1]].append(cable[0])

    def dfs(node, visited):
        visited[node] = True
        max_hops = 0
        for neighbor in graph[node]:
            if not visited[neighbor]:
                max_hops = max(max_hops, 1 + dfs(neighbor, visited))
        return max_hops

    max_hops = 0
    for i in range(computers):
        visited = [False] * computers
        max_hops = max(max_hops, dfs(i, visited))

    return max_hops

# Sample Input
computers = 6
existing_cables = [(0, 1), (0, 2), (3, 4), (3, 5)]

print(find_max_hops(computers, existing_cables))  # Output: 3
```
