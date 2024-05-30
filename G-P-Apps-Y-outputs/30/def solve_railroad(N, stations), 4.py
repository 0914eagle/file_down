
def solve_railroad(N, stations):
    times = [0] * N
    for i in range(N-1):
        for j in range(i, N-1):
            time_to_reach = max(times[j], stations[j][1])
            if time_to_reach % stations[j][2] != 0:
                time_to_reach += stations[j][2] - (time_to_reach % stations[j][2])
            time_to_reach += stations[j][0]
            times[j+1] = time_to_reach
    return times

# Input
N = 3
stations = [(6, 5, 1), (1, 10, 1)]

# Output
result = solve_railroad(N, stations)
for time in result:
    print(time)

```
