
def find_max_secure_rooms(N, M, doors):
    # Initialize a dictionary to store the rooms reachable from outside through each door
    reachable_rooms = {}
    
    # Initialize a set to store the rooms reachable from each room
    rooms_reachable_from = {}
    
    # Fill the rooms_reachable_from dictionary
    for u, v in doors:
        if u in rooms_reachable_from:
            rooms_reachable_from[u].add(v)
        else:
            rooms_reachable_from[u] = {v}
        
        if v in rooms_reachable_from:
            rooms_reachable_from[v].add(u)
        else:
            rooms_reachable_from[v] = {u}
    
    # Initialize maximum number of secure rooms
    max_secure_rooms = 0
    
    # Iterate through each door to find the number of secure rooms it provides access to
    for u, v in doors:
        if u == -1:
            secure_rooms = len(rooms_reachable_from[v])
        elif v == -1:
            secure_rooms = len(rooms_reachable_from[u])
        else:
            secure_rooms = len(rooms_reachable_from[u].intersection(rooms_reachable_from[v]))
        
        max_secure_rooms = max(max_secure_rooms, secure_rooms)
    
    return max_secure_rooms

# Read input
N, M = map(int, input().split())
doors = [tuple(map(int, input().split())) for _ in range(M)]

# Find the maximum number of secure rooms
result = find_max_secure_rooms(N, M, doors)
print(result)
```
