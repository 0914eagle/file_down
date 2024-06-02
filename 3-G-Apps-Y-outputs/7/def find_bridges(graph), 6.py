
def find_bridges(graph):
    def dfs(u, parent):
        nonlocal time
        low[u] = disc[u] = time
        time += 1
        for v in graph[u]:
            if disc[v] == -1:
                parent[v] = u
                dfs(v, parent)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    n = len(graph)
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    time = 0
    bridges = set()
    
    for u in range(n):
        if disc[u] == -1:
            dfs(u, parent)
    
    return len(bridges)

# Read input
N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Find bridges
num_bridges = find_bridges(graph)
print(num_bridges)
