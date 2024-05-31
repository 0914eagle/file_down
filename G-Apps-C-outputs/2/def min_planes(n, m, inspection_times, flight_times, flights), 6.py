
def min_planes(n, m, inspection_times, flight_times, flights):
    # Initialize a 2D list to keep track of the earliest time each plane can be used
    earliest_time = [[0] * n for _ in range(n)]
    
    # Initialize a variable to keep track of the number of planes needed
    planes_needed = 0
    
    for s, f, t in flights:
        # Check if the current flight can be done using an existing plane
        if earliest_time[s-1][f-1] <= t:
            earliest_time[s-1][f-1] = t + flight_times[s-1][f-1] + inspection_times[f-1]
        else:
            # If a new plane is needed, update the earliest time for the new plane
            planes_needed += 1
            earliest_time[s-1][f-1] = t + flight_times[s-1][f-1] + inspection_times[f-1]
    
    return planes_needed

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_planes(n, m, inspection_times, flight_times, flights))
