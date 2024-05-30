
def earliest_arrival_time(N, stations):
    times = [0] * N
    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            waiting_time = max(0, times[j] - stations[j][0])
            next_departure = (waiting_time + stations[i][2] - 1) // stations[i][2] * stations[i][2]
            times[i] = max(times[i], stations[j][0] + stations[j][1] + next_departure)

    for time in times:
        print(time)

# Parse input
N = int(input())
stations = [list(map(int, input().split())) for _ in range(N-1)]

earliest_arrival_time(N, stations)
```
