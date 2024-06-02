
def total_shower_time(N, T, times):
    total_time = 0
    prev_time = 0

    for i in range(N):
        if times[i] - prev_time >= T:
            total_time += T
        else:
            total_time += times[i] - prev_time

        prev_time = times[i]

    total_time += T

    return total_time

# Input parsing
N, T = map(int, input().split())
times = list(map(int, input().split()))

# Calculate total shower time
result = total_shower_time(N, T, times)
print(result)
