
def minimum_planes(n, m, inspection_times, flight_times, flights):
    # Create a graph to represent flight times between airports
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = flight_times[i][j]
    
    # Initialize variables
    planes_assigned = 0
    planes_in_use = {}
    
    for flight in flights:
        start, end, time = flight
        current_time = time
        
        # Check if a plane is available at the starting airport at the required time
        if start in planes_in_use:
            if planes_in_use[start] <= current_time:
                current_time += inspection_times[start]
            else:
                planes_assigned += 1
        
        # Check if a plane is available at the destination airport at the required time
        if end in planes_in_use:
            if planes_in_use[end] <= current_time + graph[start-1][end-1]:
                current_time += inspection_times[end]
            else:
                planes_assigned += 1
        
        planes_in_use[start] = current_time
        planes_in_use[end] = current_time + graph[start-1][end-1]
    
    return planes_assigned

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
print(minimum_planes(n, m, inspection_times, flight_times, flights))
