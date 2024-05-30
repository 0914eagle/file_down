
def find_earliest_time(N, train_info):
    times = [0] * N
    for i in range(N-1, 0, -1):
        for j in range(i, N-1):
            additional_time = (times[j] - train_info[j][1]) % train_info[j][2]
            times[j] += additional_time
        times[i-1] = train_info[i-1][0] + times[i]
    return times

# Input processing
N = int(input())
train_info = []
for _ in range(N-1):
    C, S, F = map(int, input().split())
    train_info.append((C, S, F))

# Find the earliest possible time to reach Station N from each station
result = find_earliest_time(N, train_info)

# Output the result
for time in result:
    print(time)

```
