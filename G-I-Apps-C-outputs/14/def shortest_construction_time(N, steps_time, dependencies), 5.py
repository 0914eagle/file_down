
def shortest_construction_time(N, steps_time, dependencies):
    dp = [0] * N
    for i in range(N):
        dp[i] = steps_time[i]
        for j in dependencies[i]:
            dp[i] = max(dp[i], dp[j] + steps_time[i])
    return dp[-1]

# Reading input
N = int(input())
steps_time = list(map(int, input().split()))
dependencies = []
for i in range(N):
    dependencies.append(list(map(int, input().split()))[1:])

# Calculating and printing the shortest construction time
result = shortest_construction_time(N, steps_time, dependencies)
print(result)
```
