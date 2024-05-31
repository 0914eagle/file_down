
def can_hit_all_targets(N, targets):
    targets.sort()
    
    for i in range(N-1):
        line_slope = float('inf')
        line_intercept = None
        remaining_targets = set(targets)
        remaining_targets.remove(targets[i])
        
        for j in range(i+1, N):
            x1, y1 = targets[i]
            x2, y2 = targets[j]
            
            if x1 == x2:
                slope = float('inf')
                intercept = x1
            else:
                slope = (y2 - y1) / (x2 - x1)
                intercept = y1 - slope*x1
            
            if slope != line_slope or intercept != line_intercept:
                line_slope = slope
                line_intercept = intercept
                remaining_targets.discard(targets[j])
            if not remaining_targets:
                return "success"
    
    return "failure"

# Reading input
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Checking if all targets can be hit
result = can_hit_all_targets(N, targets)
print(result)
