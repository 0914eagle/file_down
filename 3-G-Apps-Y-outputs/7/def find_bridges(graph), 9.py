
def find_bridges(graph):
    def dfs(node, parent):
        nonlocal time
        low[node] = disc[node] = time
        time += 1
        for neighbor in graph[node]:
            if disc[neighbor] == -1:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append((node, neighbor))
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])

    n = len(graph)
    disc = [-1] * n
    low = [-1] * n
    time = 0
    bridges = []

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return len(bridges)

# Read input
N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# Find bridges
num_bridges = find_bridges(graph)
print(num_bridges)
