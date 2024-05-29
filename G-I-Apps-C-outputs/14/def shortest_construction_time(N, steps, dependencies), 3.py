
def shortest_construction_time(N, steps, dependencies):
    time_saved = 10**6
    total_time = sum(steps)
    
    for i in range(N):
        time_saved = min(time_saved, steps[i])  # potential time saved if step i is eliminated
        for j in range(i):
            if i in dependencies[j]:
                steps[i] = min(steps[i], steps[j] + steps[i])
        
    return total_time - time_saved

# Read input
N = int(input())
steps = list(map(int, input().split()))
dependencies = []
for _ in range(N):
    c, *deps = map(int, input().split())
    dependencies.append(deps)

# Output
print(shortest_construction_time(N, steps, dependencies))
```
