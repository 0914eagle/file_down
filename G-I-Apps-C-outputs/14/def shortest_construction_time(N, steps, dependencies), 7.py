
def shortest_construction_time(N, steps, dependencies):
    def dp(node):
        if memo[node] != -1:
            return memo[node]

        max_time = 0
        for dep in dependencies[node]:
            max_time = max(max_time, dp(dep))

        memo[node] = max_time + steps[node]
        return memo[node]

    memo = [-1] * N
    return dp(N-1)

# Read input
N = int(input())
steps = list(map(int, input().split()))
dependencies = [[] for _ in range(N)]
for i in range(N):
    dependencies[i] = list(map(int, input().split()))[1:]

# Call function and output result
print(shortest_construction_time(N, steps, dependencies))
```
