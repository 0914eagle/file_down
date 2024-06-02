
def total_shower_time(N, T, t):
    total_time = T
    for i in range(1, N):
        diff = t[i] - t[i-1]
        if diff < T:
            total_time += diff
        else:
            total_time += T
    return total_time

# Input
N, T = map(int, input().split())
t = list(map(int, input().split()))

# Output
print(total_shower_time(N, T, t))
