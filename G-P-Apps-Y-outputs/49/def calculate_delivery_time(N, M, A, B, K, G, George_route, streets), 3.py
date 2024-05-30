
def calculate_delivery_time(N, M, A, B, K, G, George_route, streets):
    intersection_time = {}
    
    for a, b, l in streets:
        for i in range(l):
            if a not in intersection_time:
                intersection_time[a] = set()
            intersection_time[a].add(i)
            
            if b not in intersection_time:
                intersection_time[b] = set()
            intersection_time[b].add(i)
    
    luka_arrival_time = set(range(K, K+1001))
    george_route_set = set(George_route)
    
    min_delivery_time = float('inf')
    
    for intersection in range(1, N+1):
        if intersection in luka_arrival_time or intersection not in george_route_set:
            continue
        
        intersection_time_set = intersection_time.get(intersection, set())
        
        earliest_time = 1001
        for i in range(1000):
            if i in intersection_time_set and i < earliest_time:
                earliest_time = i
        
        delivery_time = earliest_time + 1
        
        if delivery_time < min_delivery_time:
            min_delivery_time = delivery_time
    
    return min_delivery_time

# Input parsing
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
George_route = list(map(int, input().split()))
streets = [list(map(int, input().split())) for _ in range(M)]

# Calculate and output the least amount of time Luka needs to make his delivery
result = calculate_delivery_time(N, M, A, B, K, G, George_route, streets)
print(result)
```
