
def total_shower_time(N, T, times):
    total_time = T
    prev_time = 0
    
    for i in range(1, N):
        diff = times[i] - times[i-1]
        if diff < T:
            total_time += diff
        else:
            total_time += T
    
    return total_time

# Input processing
N, T = map(int, input().split())
times = list(map(int, input().split()))

# Call the function and print the output
print(total_shower_time(N, T, times))
