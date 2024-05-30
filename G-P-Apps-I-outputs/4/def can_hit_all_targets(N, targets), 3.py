
def can_hit_all_targets(N, targets):
    targets.sort()
    
    if N <= 2:
        return "success"
    
    for i in range(N):
        for j in range(i + 1, N):
            dx = targets[j][0] - targets[i][0]
            dy = targets[j][1] - targets[i][1]
            
            potential_targets = set()
            potential_targets.add(targets[i])
            potential_targets.add(targets[j])
            
            for k in range(N):
                if (targets[k][0] - targets[i][0]) * dy == (targets[k][1] - targets[i][1]) * dx:
                    potential_targets.add(targets[k])
            
            if len(potential_targets) == N:
                return "success"
    
    return "failure"

# Input
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Output
result = can_hit_all_targets(N, targets)
print(result)
```
