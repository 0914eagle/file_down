
def shortest_construction_time(N, steps, dependencies):
    dp = [0] * N
    
    for i in range(1, N):
        dp[i] = steps[i]
        for j in dependencies[i]:
            dp[i] = max(dp[i], steps[i] + dp[j])
    
    return dp[N-1]

# Input
N = int(input().strip())
steps = list(map(int, input().strip().split()))
dependencies = [[] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().strip().split()))
    dependencies[i] = line[1:]

# Output
print(shortest_construction_time(N, steps, dependencies))
```
