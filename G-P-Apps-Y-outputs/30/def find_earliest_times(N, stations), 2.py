
def find_earliest_times(N, stations):
    times = [0] * N
    for i in range(N-1, -1, -1):
        # Calculate the time it takes to reach the next station
        for j in range(i+1, N):
            departure_time = stations[j][1]
            frequency = stations[j][2]
            closest_departure_time = (departure_time + frequency - 1) // frequency * frequency
            times[i] = max(times[i], closest_departure_time + stations[j][0])
    
    for time in times:
        print(time)

# Parse input
N = int(input())
stations = [list(map(int, input().split())) for _ in range(N-1)]

# Solve the problem
find_earliest_times(N, stations)
```
