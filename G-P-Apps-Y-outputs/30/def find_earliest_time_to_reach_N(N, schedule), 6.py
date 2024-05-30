
def find_earliest_time_to_reach_N(N, schedule):
    times = [0] * N
    for i in range(N-1, 0, -1):
        for j in range(i, N-1):
            times[i] = max(schedule[j][1], times[i] + ((times[j] - schedule[j][1]) // schedule[j][2] + 1) * schedule[j][2]) + schedule[j][0]
    return times

# Input parsing
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N-1)]

# Get the earliest possible time we can reach Station N for each station
result = find_earliest_time_to_reach_N(N, schedule)

# Output the results
for time in result:
    print(time)

```
