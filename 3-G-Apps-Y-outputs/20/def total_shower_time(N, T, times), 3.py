
def total_shower_time(N, T, times):
    total_time = T
    prev_time = 0
    for i in range(1, N):
        diff = times[i] - times[i-1]
        total_time += min(diff, T)
    return total_time

# Read input
N, T = map(int, input().split())
times = list(map(int, input().split()))

# Calculate and print total shower time
print(total_shower_time(N, T, times))
