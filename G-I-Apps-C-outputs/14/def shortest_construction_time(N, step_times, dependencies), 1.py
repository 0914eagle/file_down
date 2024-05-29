
def shortest_construction_time(N, step_times, dependencies):
    time_saved = [0] * N
    dp = [0] * N
    
    for i in range(N):
        dp[i] = step_times[i]
        
        for j in dependencies[i]:
            dp[i] = min(dp[i], dp[j] + step_times[i])
        
        time_saved[i] = step_times[i] - dp[i]
    
    return step_times[N-1] - time_saved[N-1]

# Input parsing
N = int(input())
step_times = list(map(int, input().split()))

dependencies = []
for _ in range(N):
    C, *dependencies_list = map(int, input().split())
    dependencies.append(dependencies_list)

# Output
result = shortest_construction_time(N, step_times, dependencies)
print(result)
```
