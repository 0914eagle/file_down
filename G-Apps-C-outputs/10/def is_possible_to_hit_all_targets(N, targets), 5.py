
def is_possible_to_hit_all_targets(N, targets):
    targets.sort()  # Sort the targets by x-coordinate
    if N <= 2:
        return "success"  # If there are 2 or fewer targets, it is always possible to hit all targets

    # Check if all targets are collinear
    for i in range(2, N):
        if (targets[i][0] - targets[i-2][0]) * (targets[i][1] - targets[i-1][1]) != (targets[i][1] - targets[i-2][1]) * (targets[i][0] - targets[i-1][0]):
            return "failure"  # If not collinear, cannot hit all targets with 2 shots

    return "success"  # If all targets are collinear, it is possible to hit all targets

# Input
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Output
print(is_possible_to_hit_all_targets(N, targets))
