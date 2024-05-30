
def can_hit_all_targets(N, targets):
    targets.sort()
    
    if N <= 2:
        return "success"
    
    for i in range(N-2):
        if (targets[i][1] - targets[i+1][1]) * (targets[i+1][0] - targets[i+2][0]) != (targets[i+1][1] - targets[i+2][1]) * (targets[i][0] - targets[i+1][0]):
            return "failure"
    
    return "success"

# Read input
N = int(input())
targets = [tuple(map(int, input().split())) for _ in range(N)]

# Check if it is possible to hit all targets
result = can_hit_all_targets(N, targets)
print(result)
```
