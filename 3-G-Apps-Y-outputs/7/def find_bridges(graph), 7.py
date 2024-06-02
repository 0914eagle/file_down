
def find_bridges(graph):
    def dfs(u, p):
        nonlocal time
        low[u] = disc[u] = time
        time += 1
        for v in graph[u]:
            if v == p:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            else:
                low[u] = min(low[u], disc[v])

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
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# Find bridges
num_bridges = find_bridges(graph)
print(num_bridges)