
def min_planes(n, m, inspection_times, flight_times, flights):
    # Create a graph representing flight times between airports
    graph = {}
    for i in range(n):
        graph[i] = {}
        for j in range(n):
            graph[i][j] = flight_times[i][j]

    # Initialize a variable to keep track of the maximum time a plane spends at each airport
    max_inspection_time = max(inspection_times)

    # Initialize a variable to keep track of the current time at each airport
    current_time = [0] * n

    # Initialize a variable to keep track of the planes available at each airport
    planes_available = [0] * n

    # Initialize a variable to keep track of the number of planes needed
    planes_needed = 0

    for i in range(m):
        start, end, time = flights[i]
        start -= 1
        end -= 1

        # Check if there is a plane available at the starting airport at the current time
        if planes_available[start] <= current_time[start]:
            planes_needed += 1

        # Update the current time at the starting airport
        current_time[start] = max(current_time[start], time + flight_times[start][end] + inspection_times[end])

        # Update the availability of a plane at the ending airport
        planes_available[end] = max(planes_available[end], current_time[end] + max_inspection_time)

    return planes_needed

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
print(min_planes(n, m, inspection_times, flight_times, flights))
