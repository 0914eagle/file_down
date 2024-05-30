
def find_earliest_time(N, trains):
    times = [0] * N
    for i in range(N-1, 0, -1):
        for j in range(i, N):
            if j == i:
                times[j] = max(trains[j][1], times[j])
            else:
                wait_time = max(0, times[j] - (times[j] - trains[j][1]) % trains[j][2])
                times[j] = max(wait_time + trains[j][0], times[j])
    return times

N = int(input())
trains = [tuple(map(int, input().split())) for _ in range(N-1)]

result = find_earliest_time(N, trains)
for time in result:
    print(time)

```
