
def bfs(graph, start, target):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node == target:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False
def solve(n, m, edges):
    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    for i in range(n):
        if not bfs(graph, i, i):
            return "impossible"
    
    return n

