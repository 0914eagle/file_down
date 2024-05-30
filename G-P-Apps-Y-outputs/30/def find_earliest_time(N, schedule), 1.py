
def find_earliest_time(N, schedule):
    times = [0] * N
    for i in range(N-1, 0, -1):
        for j in range(i, N-1):
            wait_time = max(0, times[j] - schedule[j][1])  # waiting time for previous train
            times[j] = schedule[j][1] + schedule[j][0] + ((wait_time + schedule[j][2] - 1) // schedule[j][2]) * schedule[j][2]
        times[i-1] = schedule[i-1][1] + schedule[i-1][0]
    
    for t in times:
        print(t)

# Input processing
N = int(input())
schedule = []
for _ in range(N-1):
    C, S, F = map(int, input().split())
    schedule.append((C, S, F))

find_earliest_time(N, schedule)
```
