
def find_bridges(graph):
    def dfs(node, parent, visited, low, disc, bridges):
        nonlocal time
        visited[node] = True
        disc[node] = time
        low[node] = time
        time += 1
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, node, visited, low, disc, bridges)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append((node, neighbor))
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])
    
    n = len(graph)
    visited = [False] * n
    disc = [-1] * n
    low = [-1] * n
    time = 0
    bridges = []
    
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, visited, low, disc, bridges)
    
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
