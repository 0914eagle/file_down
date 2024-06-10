
n, m, alpha = map(int, input().split())
roads = []
for _ in range(m):
    u, v, c = map(int, input().split())
    roads.append([u, v, c])

graph = [[] for _ in range(n + 1)]
for u, v, c in roads:
    graph[u].append([v, c])
    graph[v].append([u, c])
    
def bfs(graph, start, end):
    queue = [[start, 0, []]]
    visited = [False] * (n + 1)
    visited[start] = True
    
    while queue:
        node, cost, path = queue.pop(0)
        
        if node == end:
            return cost, path
        
        for neighbor, candy in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append([neighbor, cost + candy, path + [neighbor]])
    
    return None, None
    
cost, path = bfs(graph, 1, 1)
if cost is None:
    print("Poor girl")
else:
    print(cost ** 2 + alpha * (len(path) - 1))

