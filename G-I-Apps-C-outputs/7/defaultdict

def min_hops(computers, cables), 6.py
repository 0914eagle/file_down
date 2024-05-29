
from collections import defaultdict

def min_hops(computers, cables):
    graph = defaultdict(list)
    for a, b in cables:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(node):
        visited = set()
        queue = [(node, 0)]
        max_hops = 0
        while queue:
            curr_node, hops = queue.pop(0)
            visited.add(curr_node)
            max_hops = max(max_hops, hops)
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    queue.append((neighbor, hops + 1))
        return max_hops

    max_hops = 0
    for node in range(computers):
        max_hops = max(max_hops, bfs(node))

    return max_hops

# Sample Input
computers = 6
cables = [(0, 1), (0, 2), (3, 4), (3, 5)]

print(min_hops(computers, cables))  # Output: 3
```
