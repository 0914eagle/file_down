
def max_protected_rooms(N, M, doors):
    graph = {}
    for u, v in doors:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)

    num_protected = 0
    for u, v in doors:
        rooms_reachable = set()
        if u == -1:
            rooms_reachable.add(v)
            dfs(v, graph, rooms_reachable)
        elif v == -1:
            rooms_reachable.add(u)
            dfs(u, graph, rooms_reachable)
        
        if len(rooms_reachable) < N:
            num_protected = max(num_protected, N - len(rooms_reachable))
    
    return num_protected

def dfs(room, graph, rooms_reachable):
    rooms_reachable.add(room)
    for neighbor in graph.get(room, []):
        if neighbor not in rooms_reachable:
            dfs(neighbor, graph, rooms_reachable)

# Input parsing
N, M = map(int, input().split())
doors = [tuple(map(int, input().split())) for _ in range(M)]

result = max_protected_rooms(N, M, doors)
print(result)
