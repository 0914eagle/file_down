
def can_hit_all_targets(N, targets):
    # Sort targets by x-coordinate
    sorted_targets = sorted(targets, key=lambda x: x[0])

    # Check if all targets lie on a straight line
    for i in range(1, N - 1):
        if (sorted_targets[i][1] - sorted_targets[0][1]) * (sorted_targets[N - 1][0] - sorted_targets[0][0]) != (sorted_targets[N - 1][1] - sorted_targets[0][1]) * (sorted_targets[i][0] - sorted_targets[0][0]):
            return "failure"

    return "success"

# Input processing
N = int(input())
targets = [list(map(int, input().split())) for _ in range(N)]

# Call function and print output
print(can_hit_all_targets(N, targets))
```
