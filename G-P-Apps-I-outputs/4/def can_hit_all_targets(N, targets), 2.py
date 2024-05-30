
def can_hit_all_targets(N, targets):
    targets.sort()
    
    # Check if there are less than 3 targets
    if N <= 2:
        return "success"
    
    for i in range(1, N - 1):
        x1, y1 = targets[0]
        x2, y2 = targets[i]
        slope = float(y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
        temp_targets = set()
        temp_targets.add((x1, y1))
        temp_targets.add((x2, y2))
        
        for j in range(N):
            if j == 0 or j == i:
                continue
            x, y = targets[j]
            if x1 != x:
                new_slope = float(y - y1) / (x - x1)
            else:
                new_slope = float('inf')

            if new_slope == slope:
                temp_targets.add((x, y))
        
        if len(temp_targets) == N:
            return "success"
    
    return "failure"

# Read input
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Check if it is possible to hit all targets
result = can_hit_all_targets(N, targets)
print(result)
```
