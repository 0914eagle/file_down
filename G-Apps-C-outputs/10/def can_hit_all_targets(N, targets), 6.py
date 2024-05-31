
def can_hit_all_targets(N, targets):
    targets.sort()  # Sorting the targets by x-coordinate
    for i in range(N - 2):
        x1, y1 = targets[i]
        x2, y2 = targets[i + 1]
        x3, y3 = targets[i + 2]
        
        # Checking if the three consecutive targets are collinear
        if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
            return "failure"
    
    return "success"

# Reading input
N = int(input())
targets = [list(map(int, input().split())) for _ in range(N)]

# Checking if it is possible to hit all targets
result = can_hit_all_targets(N, targets)
print(result)
