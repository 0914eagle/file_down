
def can_hit_all_targets(N, targets):
    targets.sort()  # Sort targets based on their x-coordinate
    if N == 1:  # If only one target, success
        return "success"
    
    for i in range(N-1):
        x1, y1 = targets[i]
        x2, y2 = targets[i+1]
        
        # Calculate slope between two adjacent targets
        if x2 - x1 == 0:
            slope = float('inf')
        else:
            slope = (y2 - y1) / (x2 - x1)
        
        # Check if all targets lie on the same line
        for j in range(i+2, N):
            x3, y3 = targets[j]
            if x2 - x3 == 0:
                slope_new = float('inf')
            else:
                slope_new = (y3 - y2) / (x3 - x2)
            if slope_new != slope:
                return "failure"
    
    return "success"

# Input parsing
N = int(input())
targets = [list(map(int, input().split())) for _ in range(N)]

# Check if it is possible to hit all targets
result = can_hit_all_targets(N, targets)
print(result)
```
