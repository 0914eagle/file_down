
def can_hit_all_targets(N, targets):
    if N <= 2:
        return "success"
    
    targets.sort()
    
    for i in range(N - 2):
        x1, y1 = targets[i]
        x2, y2 = targets[i + 1]
        x3, y3 = targets[i + 2]
        
        if (y3 - y1) * (x2 - x1) != (y2 - y1) * (x3 - x1):
            return "failure"
    
    return "success"

# Reading input
N = int(input())
targets = [tuple(map(int, input().split())) for _ in range(N)]

# Calling the function and printing the result
print(can_hit_all_targets(N, targets))
