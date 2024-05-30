
def calculate_delivery_time(N, M, A, B, K, G, george_route, streets):
    intersections = {}
    for i in range(1, N + 1):
        intersections[i] = float('inf')
    
    intersections[A] = K
    queue = [(A, K)]
    
    while queue:
        current_intersection, current_time = queue.pop(0)
        
        for street in streets:
            if current_intersection in street[:2]:
                next_intersection = street[0] if street[1] == current_intersection else street[1]
                traversal_time = street[2]
                
                for t in range(current_time, current_time + traversal_time):
                    if t < intersections[next_intersection]:
                        intersections[next_intersection] = t

                queue.append((next_intersection, intersections[next_intersection]))
    
    delivery_time = float('inf')
    
    for i in range(0, 2 * G, 2):
        intersection = george_route[i]
        if intersections[intersection] < delivery_time:
            delivery_time = intersections[intersection]
    
    return delivery_time

# Input parsing
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
george_route = list(map(int, input().split()))
streets = [list(map(int, input().split())) for _ in range(M)]

# Calculate and output the least amount of time Luka needs to make his delivery
print(calculate_delivery_time(N, M, A, B, K, G, george_route, streets))
```
