
def can_hit_all_targets(N, targets):
    targets.sort()  # Sort the targets by x-coordinate

    for i in range(N - 1):
        # Calculate the slope of the line passing through targets[i] and targets[i+1]
        slope = (targets[i+1][1] - targets[i][1]) / (targets[i+1][0] - targets[i][0]) if targets[i+1][0] - targets[i][0] != 0 else float('inf')

        # Check if all other targets lie on the same line
        for j in range(i + 2, N):
            if (targets[j][0] - targets[i][0]) * (targets[j][1] - targets[i][1]) != (targets[j][1] - targets[i][1]) * (targets[i][0] - targets[i][0] if targets[i+1][0] - targets[i][0] != 0 else float('inf')):
                return "failure"

    return "success"

# Read input
N = int(input())
targets = [list(map(int, input().split())) for _ in range(N)]

# Check if it is possible to hit all targets with at most two shots
result = can_hit_all_targets(N, targets)
print(result)
```
