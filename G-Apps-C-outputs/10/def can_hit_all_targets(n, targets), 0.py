
def can_hit_all_targets(n, targets):
    targets.sort()
    
    for i in range(n-1):
        x1, y1 = targets[i]
        x2, y2 = targets[i+1]
        
        dx = x2 - x1
        dy = y2 - y1
        
        # Check if all targets are in a straight line
        for j in range(i+2, n):
            x3, y3 = targets[j]
            if dx*(y3-y1) != dy*(x3-x1):
                return "failure"
    
    return "success"

# Read input
n = int(input())
targets = []
for _ in range(n):
    x, y = map(int, input().split())
    targets.append((x, y))

# Call the function and print the result
result = can_hit_all_targets(n, targets)
print(result)
