
def earliest_arrival_time(N, stations):
    times = [0] * N
    for i in range(N - 1, 0, -1):
        for j in range(i, N - 1):
            times[i-1] = max(stations[j][1], ((times[j] - stations[j][1]) // stations[j][2] + 1) * stations[j][2] + stations[j][0])
    return times

# Read input
N = int(input())
stations = [list(map(int, input().split())) for _ in range(N-1)]

# Calculate and output the earliest arrival times
result = earliest_arrival_time(N, stations)
for x in result:
    print(x)
```
