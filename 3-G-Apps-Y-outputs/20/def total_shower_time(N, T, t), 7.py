
def total_shower_time(N, T, t):
    total_time = T
    for i in range(1, N):
        if t[i] - t[i-1] < T:
            total_time += t[i] - t[i-1]
        else:
            total_time += T
    return total_time

# Reading input
N, T = map(int, input().split())
t = list(map(int, input().split()))

# Calculating and printing the total shower time
print(total_shower_time(N, T, t))
