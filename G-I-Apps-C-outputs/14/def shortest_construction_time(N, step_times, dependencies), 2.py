
def shortest_construction_time(N, step_times, dependencies):
    dp = [0] * N
    for i in range(N):
        time = step_times[i]
        for j in dependencies[i]:
            time = max(time, dp[j])
        dp[i] = time + step_times[i]
    
    return dp[-1]

# Input
N = 2
step_times = [15, 20]
dependencies = [[], [0]]

# Output
result = shortest_construction_time(N, step_times, dependencies)
print(result)
