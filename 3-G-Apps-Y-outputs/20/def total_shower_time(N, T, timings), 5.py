
def total_shower_time(N, T, timings):
    total_time = T
    prev_time = 0
    for i in range(1, N):
        diff = timings[i] - timings[i-1]
        if diff < T:
            total_time += diff
        else:
            total_time += T
    return total_time

# Input processing
N, T = map(int, input().split())
timings = list(map(int, input().split()))

# Calculate total shower time
result = total_shower_time(N, T, timings)
print(result)
