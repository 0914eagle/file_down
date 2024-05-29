
def max_secure_rooms(N, M, doors):
    rooms_connected_to_outside = set()
    room_connections = dict()

    for door in doors:
        u, v = door
        if u == -1:
            rooms_connected_to_outside.add(v)
        elif v == -1:
            rooms_connected_to_outside.add(u)
        else:
            if u not in room_connections:
                room_connections[u] = set()
            if v not in room_connections:
                room_connections[v] = set()

            room_connections[u].add(v)
            room_connections[v].add(u)

    max_rooms_protected = 0

    for room in room_connections:
        if room not in rooms_connected_to_outside:
            num_protected = 0
            visited = set()

            def dfs(current_room):
                nonlocal num_protected
                visited.add(current_room)
                num_protected += 1

                if current_room in room_connections:
                    for neighbor in room_connections[current_room]:
                        if neighbor not in visited:
                            dfs(neighbor)

            dfs(room)
            max_rooms_protected = max(max_rooms_protected, num_protected)

    return max_rooms_protected

# Sample input
N = 2
M = 3
doors = [(-1, 0), (-1, 1), (0, 1)]

print(max_secure_rooms(N, M, doors))  # Output: 0
```
