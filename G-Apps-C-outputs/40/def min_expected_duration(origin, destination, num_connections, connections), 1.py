
import heapq

def min_expected_duration(origin, destination, num_connections, connections):
    graph = {}
    
    for connection in connections:
        start, end, departure_time, journey_time, probability, max_delay = connection
        
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        
        graph[start][(start, end, departure_time)] = [(journey_time, probability, max_delay)]
    
    pq = [(0, origin, 0)]
    visited = set()
    
    while pq:
        time, current, delay = heapq.heappop(pq)
        
        if current == destination:
            return time
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current in graph:
            for (start, end, departure_time), details in graph[current].items():
                new_time = time + departure_time - delay
                for journey_time, probability, max_delay in details:
                    new_delay = delay
                    
                    if probability > 0:
                        expected_delay = probability * max_delay / 100
                        new_delay += expected_delay
                    
                    heapq.heappush(pq, (new_time + journey_time + new_delay, end, new_delay))
    
    return "IMPOSSIBLE"

# Input parsing
origin, destination = input().split()
num_connections = int(input())
connections = []

for _ in range(num_connections):
    connection = input().split()
    connections.append((connection[0], connection[1], int(connection[2]), int(connection[3]), int(connection[4]), int(connection[5])))

# Call the function
result = min_expected_duration(origin, destination, num_connections, connections)
print(result)
