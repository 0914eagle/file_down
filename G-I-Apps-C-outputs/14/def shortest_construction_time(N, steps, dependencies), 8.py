
def shortest_construction_time(N, steps, dependencies):
    def dfs(step, dp, steps, dependencies):
        if dp[step] != -1:
            return dp[step]
        
        max_time = steps[step]
        for dep_step in dependencies[step]:
            max_time = max(max_time, steps[step] + dfs(dep_step, dp, steps, dependencies))
        
        dp[step] = max_time
        return max_time
    
    dp = [-1] * N
    return steps[0] + dfs(N-1, dp, steps, dependencies)

# Input parsing
N = int(input())
steps = list(map(int, input().split()))
dependencies = [[] for _ in range(N)]
for i in range(N):
    nums = list(map(int, input().split()))
    dependencies[i] = nums[1:]

result = shortest_construction_time(N, steps, dependencies)
print(result)
```
