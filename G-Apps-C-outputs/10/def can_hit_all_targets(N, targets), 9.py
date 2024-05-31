
def can_hit_all_targets(N, targets):
    targets.sort()  # Sort the targets by x-coordinate

    # Check if all targets are on the same line
    def on_same_line(p1, p2, p3):
        return (p3[1] - p1[1]) * (p2[0] - p1[0]) == (p2[1] - p1[1]) * (p3[0] - p1[0])

    for i in range(N - 2):
        if on_same_line(targets[i], targets[i + 1], targets[i + 2]):
            continue
        else:
            return "failure"

    return "success"

# Read input
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Call the function and output the result
print(can_hit_all_targets(N, targets))
