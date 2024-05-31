
def can_hit_all_targets(N, targets):
    targets.sort()  # Sort the targets based on x-coordinate
    if N <= 2:
        return "success"  # If there are 2 or fewer targets, we can always hit them with at most 2 shots

    for i in range(N - 2):
        x1, y1 = targets[i]
        x2, y2 = targets[i + 1]
        x3, y3 = targets[i + 2]
        
        # Check if the three targets are collinear
        if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
            return "success"
    
    return "failure"

# Input processing
N = int(input())
targets = []
for _ in range(N):
    X, Y = map(int, input().split())
    targets.append((X, Y))

# Call the function and print the result
print(can_hit_all_targets(N, targets))
