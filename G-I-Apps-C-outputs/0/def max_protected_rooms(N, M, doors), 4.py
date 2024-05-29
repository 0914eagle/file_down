
def max_protected_rooms(N, M, doors):
    connections = {}
    for door in doors:
        u, v = door
        if u not in connections:
            connections[u] = set()
        if v not in connections:
            connections[v] = set()
        connections[u].add(v)
        connections[v].add(u)
    
    max_protected = 0
    for u in range(N):
        if u in connections:
            reachable_rooms = set()
            for v in connections[u]:
                if v != -1:
                    reachable_rooms.add(v)
            if len(reachable_rooms) > max_protected:
                max_protected = len(reachable_rooms)
    
    return max_protected

# Sample Input
N = 2
M = 3
doors = [(-1, 0), (-1, 1), (0, 1)]

print(max_protected_rooms(N, M, doors))  # Sample Output: 0
