
import math

def earliest_time_to_reach_destination(N, schedule):
    arrival_times = [0] * N

    for i in range(N-1):
        for j in range(i, N-1):
            wait_time = max(0, arrival_times[j] - schedule[j][1])  # wait time for the next train
            next_departure = math.ceil((arrival_times[j] + wait_time) / schedule[j][2]) * schedule[j][2]
            arrival_times[j+1] = max(arrival_times[j+1], next_departure + schedule[j][0])

    return arrival_times

# Input parsing
N = int(input())
schedule = []
for _ in range(N-1):
    c, s, f = map(int, input().split())
    schedule.append((c, s, f))

# Calculate earliest times
result = earliest_time_to_reach_destination(N, schedule)

# Output
for time in result:
    print(time)

```
