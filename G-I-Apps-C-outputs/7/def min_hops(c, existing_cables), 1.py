
def min_hops(c, existing_cables):
    adj_list = {i: set() for i in range(c)}
    for a, b in existing_cables:
        adj_list[a].add(b)
        adj_list[b].add(a)

    def bfs(node):
        visited = set()
        queue = [(node, 0)]
        max_hops = 0

        while queue:
            curr_node, hops = queue.pop(0)
            max_hops = max(max_hops, hops)

            for neighbor in adj_list[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, hops + 1))

        return max_hops

    max_hops = 0
    for i in range(c):
        max_hops = max(max_hops, bfs(i))

    return max_hops

# Sample input
c = 6
existing_cables = [(0, 1), (0, 2), (3, 4), (3, 5)]

print(min_hops(c, existing_cables))  # Output: 3
```
