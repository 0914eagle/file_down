
def can_hit_all_targets(N, targets):
    if N <= 2:
        return "success"
    
    targets.sort()
    
    for i in range(N-1):
        x1, y1 = targets[i]
        x2, y2 = targets[i+1]
        
        dx = x2 - x1
        dy = y2 - y1
        
        potential_targets = set([(x1 + k*dx, y1 + k*dy) for k in range(1, N)])
        if potential_targets.issubset(set(targets)):
            return "success"
    
    return "failure"

# Input parsing
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))
    
# Check if it is possible to hit all targets
result = can_hit_all_targets(N, targets)
print(result)
