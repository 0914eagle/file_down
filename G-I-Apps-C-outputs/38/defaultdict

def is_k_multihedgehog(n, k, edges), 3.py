
from collections import defaultdict

def is_k_multihedgehog(n, k, edges):
    adjacency_list = defaultdict(list)
    degrees = [0] * (n + 1)

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    center = None
    for i in range(1, n + 1):
        if degrees[i] >= 3:
            center = i
            break

    if center is None or k == 1:
        return "No"

    queue = [center]
    visited = {center}
    layers_remaining = k - 1

    while queue and layers_remaining > 0:
        new_queue = []
        for node in queue:
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_queue.append(neighbor)
        queue = new_queue
        layers_remaining -= 1

    return "Yes" if len(visited) == n else "No"

# Input parsing
n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Check if the graph is a k-multihedgehog
result = is_k_multihedgehog(n, k, edges)
print(result)
