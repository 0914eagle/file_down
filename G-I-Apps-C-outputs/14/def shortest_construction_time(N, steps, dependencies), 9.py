
def shortest_construction_time(N, steps, dependencies):
    times = [0] * N
    for i in range(N):
        times[i] = steps[i]
        for j in dependencies[i]:
            times[i] = max(times[i], times[j - 1] + steps[i])
    
    return times[-1]

# Input parsing
N = int(input())
steps = list(map(int, input().split()))
dependencies = [[] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    dependencies[i] = line[1:]

# Call the function and print the output
print(shortest_construction_time(N, steps, dependencies))
```
